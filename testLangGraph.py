from typing import Annotated, List
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END   # ⭐ 匯入 START / END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage

# reducer：保留最新值
def last_value(_, new):
    return new

# ─────────────────────────────────────────────────────────────
# 1. 定義 State schema
# ─────────────────────────────────────────────────────────────
class MyState(BaseModel):
    value:   Annotated[str, last_value]
    count:   Annotated[int, last_value]
    message: Annotated[List[HumanMessage], add_messages]

# ─────────────────────────────────────────────────────────────
# 2. 建立 Graph Builder
# ─────────────────────────────────────────────────────────────
builder = StateGraph(MyState)

# ─────────────────────────────────────────────────────────────
# 3. 節點定義
# ─────────────────────────────────────────────────────────────
def process_node(state: MyState) -> dict:
    new_cnt = state.count + 1
    msg = f"Process #{new_cnt} done"
    print(f"[Node] {msg}")
    return {
        "value":   f"Processed_{new_cnt}",
        "count":   new_cnt,
        "message": [HumanMessage(content=msg)],
    }

def complete_node(state: MyState) -> dict:
    msg = "Workflow completed"
    print(f"[End] {msg}")
    return {
        "value":   "Completed",
        "count":   state.count,
        "message": [HumanMessage(content=msg)],
    }

builder.add_node("process", process_node)
builder.add_node("complete", complete_node)

# ─────────────────────────────────────────────────────────────
# 4. 連接邊：用 START / END
# ─────────────────────────────────────────────────────────────
def counter(state: MyState) -> str:
    """跑滿 3 次就跳到 complete，否則留在 process"""
    return "complete" if state.count >= 3 else "process"

# 入口：START ➜ process
builder.add_edge(START, "process")

# # 由 process 依條件前往 process 或 complete
builder.add_conditional_edges("process", counter, ["process", "complete"])

# 終點：complete ➜ END
builder.add_edge("complete", END)

# ─────────────────────────────────────────────────────────────
# 5. 編譯並執行
# ─────────────────────────────────────────────────────────────
app = builder.compile()

## # 取得 Mermaid 圖表文字
## # 這樣可以視覺化整個流程圖
## 🧩 這個文字可以貼到： https://mermaid.live 線上工具
mermaid_text = app.get_graph().draw_mermaid()
print(mermaid_text, "\n🧩 文字可以貼到： https://mermaid.live", "\n")


initial_state = MyState(value="initial", count=0, message=[])
final_state_dict = app.invoke(initial_state)   # 最終結果（dict）

# ─────────────────────────────────────────────────────────────
# 6. 逐步列印所有中間狀態
# ─────────────────────────────────────────────────────────────

# 轉回 MyState 物件
final_state = MyState(**final_state_dict)
print("\n✅ Final state:", 
      "\n  | value:", final_state.value,
      "\n  | count:", final_state.count,
      "\n  | messages:", [m.content for m in final_state.message])

# 列印逐步狀態
print("\n📘 逐步狀態：")
for i, step in enumerate(app.stream(initial_state)):
    if 'complete' in step:
        step = step['complete']
    else:
        step = step['process']

    print(f"Step {i+1:>2} → value={step['value']}, count={step['count']}, "
        f"message={[m.content for m in step['message']]}")
