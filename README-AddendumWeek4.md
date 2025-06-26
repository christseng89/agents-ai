# Week 4 - LangGraph

## Week 4 Day 1
### **LangGraph - 🧠 本週概覽

* 第 4 週相對較短，因為前三週已深入探索過 **OpenAI Agents SDK** 和 **Crew**。
* 本週重點：轉向 **LangGraph**，這是一種全新的思維方式和技術架構。
* 最終你將會看到一個**真正有商業價值的應用實例**，從中受益。

---

### 🤯 LangChain Ecosystem 生態系統的迷思解釋

| 名稱            | 解釋                                       |
| ------------- | ---------------------------------------- |
| **LangChain** | 最早的框架，專注於 **LLM 整合、工具調用與記憶管理**等抽象化工具。        |
| **LangGraph** | 用於構建**穩定、可擴展、多代理人流程**的**圖形式框架**。             |
| **LangSmith** | 專門用來**監控與除錯** LangChain 或 LangGraph 的工具。 |

#### 📦 LangChain 重點特性：

* 支援 Prompt Templates、記憶體模型、RAG 管線等。
* 提供了許多「開箱即用」的抽象工具來快速構建應用。
* 缺點：抽象層多 → 開發者對 Prompt 與流程可見度較低。

---

### 📈 什麼是 LangGraph？

LangGraph 是 **LangChain 團隊**推出的獨立框架，設計理念與 LangChain 不同：

| 特性 | 說明                                     |
| -- | -------------------------------------- |
| 目標 | 構建**穩定、可觀測、可擴展**的多代理任務工作流              |
| 架構 | 圍繞 **Graph 結構（有向圖）**，每個節點是一個流程步驟       |
| 優勢 | 支援「人機協作」、「記憶體」、「歷史追蹤」、「錯誤容忍」、「時光回溯」等功能 |
| 類比 | 更像是你可以部署的「代理人編排平台」                     |

- LangGraph 適合用於那些需要**複雜決策邏輯與多階段代理互動**的場景。
- **LangGraph 提供 Agent-driven UX（以代理人為驅動的使用者體驗）設計能力**，這也是它最強大的核心之一。
---

### 🔍 LangGraph vs LangChain

| 功能    | LangChain      | LangGraph       |
| ----- | -------------- | --------------- |
| 概念基礎  | Prompt & Chain | **Workflow Graph**  |
| 抽象目標  | 提供工具集合         | 提供流程結構與穩定執行     |
| 適合對象  | 快速整合 LLM 的開發者  | 需要**流程**可靠性與**監控**的企業應用 |
| 監控支援  | 搭配 LangSmith   | 搭配 LangSmith    |
| 記憶體管理 | 有（內建）          | 可接入外部記憶體或工具     |

---

### 🧩 結語

* 本週我們將用 **LangGraph** 實作一個高可靠性的 AI 代理系統。
* 接下來你會看到如何使用圖（Graph）來組織整個流程。
* 這將讓你能夠構建具備「回溯能力」與「可觀測性」的智能應用。
* 我們也會整合 **LangSmith** 來監控代理行為與 LLM 輸出。

---
#### ✅ 為什麼大多數 LLM 遵循 OpenAI API 標準？

**大部分現代 LLM（大型語言模型）平台都在逐步採用或兼容 OpenAI 的 API 標準**，這個趨勢相當明顯，主要原因如下：


| 原因                                                             | 說明                                                                           |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **1. OpenAI API 成為事實上的業界標準**                                   | OpenAI 的 API（特別是 `chat/completions` 與 `completions` 接口）使用簡單、清晰，已被大量開發者與工具採用。 |
| **2. 開發者生態龐大**                                                 | 支援 OpenAI API 就能立即使用數萬套現有的 SDK、代理框架（如 LangChain、CrewAI、LangGraph）與工具鏈。       |
| **3. 降低遷移成本**                                                  | 如果使用者原本用的是 GPT 模型，現在要切換成別的模型（如 Claude、Gemini、Mistral）時，只要 API 相容，就幾乎不需改代碼。   |
| **4. 多數開源模型的 API Proxy（如 Ollama、vLLM、LM Studio）也模擬 OpenAI 格式** | 例如你在本地部署 LLM，也可模擬出 `POST /v1/chat/completions` 等接口，達到與 OpenAI 相同體驗。          |

---

## 🧩 哪些 LLM 提供 OpenAI 相容 API？

| 廠商 / 平台                                | 是否相容 OpenAI API                    | 備註                                                  |
| -------------------------------------- | ---------------------------------- | --------------------------------------------------- |
| **Anthropic Claude 3**                 | ✅（透過 OpenRouter、Fireworks.ai 等提供者） | 本身 API 結構不同，但中介服務支援轉換                               |
| **Google Gemini**                      | ⚠️ 部分相容                            | Gemini 自有 API 為主（Google AI Studio），尚未完全模擬 OpenAI 結構 |
| **Mistral (via Lepton.ai, Fireworks)** | ✅                                  | 提供 chat-completion 格式                               |
| **Groq + Mixtral**                     | ✅                                  | 高速推理，支援 OpenAI 接口                                   |
| **Together.ai**                        | ✅                                  | 提供幾十種模型，均以 OpenAI API 格式調用                          |
| **OpenRouter.ai**                      | ✅                                  | 聚合多模型，使用統一 OpenAI API 格式                            |
| **LM Studio / Local LLM**              | ✅（支援 OpenAI Proxy）                 | 可離線使用 HuggingFace 模型，模擬 chat API                    |

---

## 💬 OpenAI API 標準範例（`/v1/chat/completions`）

```json
POST /v1/chat/completions
{
  "model": "gpt-4",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather today?"}
  ],
  "temperature": 0.7
}
```

---

## 🔄 相容的好處

* ✅ 更容易切換模型（vendor lock-in 風險降低）
* ✅ 相容 CrewAI、LangGraph、LangChain、LlamaIndex 等框架
* ✅ 可使用既有的工具如 `litellm`、`llama-cpp-python`、`openai-python` 直接調用

---

### ✅ 結論

> 是的，**大多數 LLM 提供商（尤其是開源與多模型平台）正逐步支援或模擬 OpenAI API 格式**，這已成為跨平台整合與多代理人架構中的主流溝通標準。 如果想在不同模型之間切換而不改動程式碼，OpenAI API 標準是一個很好的選擇。

---

#### ✅ 什麼是 Agent-driven UX？

Agent-driven UX 指的是：

> **使用者與多個 AI 代理人互動時，這些代理人會根據上下文、記憶體與任務狀態主動回應、調整流程，甚至彼此協作完成任務。**

LangGraph 讓你可以把這些代理人和流程視為「圖（Graph）節點」，建立一種 **可追蹤、可擴展、容錯性高的工作流體驗**。

---

## 📌 舉個例子來說明：智能客戶服務系統

### 🎯 使用情境：線上銀行 App 的智能客服

---

### 👤 使用者需求流程（UX）

1. 使用者：「我想知道我的信用卡帳單」
2. 系統自動：

   * 啟動「身份驗證代理人」請求驗證碼
   * 身份驗證成功後，觸發「查詢帳單代理人」
   * 若金額超標，觸發「理財建議代理人」
   * 結果彙整後，回覆使用者完整資訊與建議

---

### 🔁 LangGraph 的圖形結構會長這樣：

```
[Start]
   ↓
[身份驗證代理人]
   ↓ success
[查詢帳單代理人]
   ↓ 條件：帳單高
[理財建議代理人]
   ↓
[總結回覆代理人]
```

每個節點就是一個 Agent（代理人），由 LangGraph 控制流程和分支。

---

### ✨ LangGraph 的貢獻

| 功能                     | 說明                                |
| ---------------------- | --------------------------------- |
| **節點式流程圖（Node Graph）** | 每個代理人是一個節點，定義好輸入/輸出條件即可組裝         |
| **Human-in-the-loop**  | 任意節點可加入「人工審核」步驟（如身分驗證）            |
| **記憶體追蹤**              | 保留上下文與歷史對話，讓代理人具備延續性              |
| **時光回溯（Time Travel）**  | 若流程出錯可返回任一節點重跑（Checkpoints）       |
| **錯誤容忍與復原**            | 系統出現錯誤可自動回復流程、重啟節點                |
| **與 LangSmith 整合**     | 可觀察每一個節點的 LLM 輸入與輸出、Token 消耗與錯誤紀錄 |

---

## ✅ 小結

是的，**LangGraph 不只是支援 Agent，更讓你打造一整套基於代理人的 UX 流程**，舉凡：

* 金融客服系統
* 醫療問診流程
* 招聘自動化面試助手
* 企業文件自動審核與彙整流程
* 電商訂單查詢 + 退貨流程 + 銷售建議

都可以透過 LangGraph 的圖式流程與多代理控制來實現。

---

### **LangGraph** 系列產品中三個名詞的定位說明與差異解析：

## 🔶 1. **LangGraph**

> 🔹 **定位**：核心開源框架（Python Library）
> 🔹 功能：定義並執行基於「有向圖（Graph）」的多代理人 AI 工作流

| 項目      | 說明                                       |
| ------- | ---------------------------------------- |
| 📦 類型   | 開源 Python 套件（`pip install langgraph`）    |
| 🧠 本質   | 把任務與狀態視為**節點**串成可視化流程圖                     |
| 🔁 支援功能 | 狀態機、記憶體管理、回滾（checkpoint）、callback 任務動態生成 |
| ✅ 適用場景  | 架設穩定可控的 Agent Workflow（如客戶服務流程、醫療問診系統）   |

---

## 🟠 2. **LangGraph Studio**

> 🔹 **定位**：視覺化設計工具（**低代碼/無代碼**編輯器）
> 🔹 功能：用 GUI 拖拉節點建立 LangGraph 工作流，無需直接編寫程式碼

| 項目      | 說明                                            |
| ------- | --------------------------------------------- |
| 🖥 類型   | 雲端平台介面（類似 VS Code for Graph）                  |
| 🧱 功能特點 | 節點編輯器、路徑連接器、輸入輸出條件設定                          |
| 🪄 對象   | 非技術使用者 / 業務分析師 / Product Manager              |
| 🔗 關係   | 編輯的工作流可以導出為 Python 程式碼或部署到 LangGraph Platform |

---

## 🔵 3. **LangGraph Platform**

> 🔹 **定位**：企業級部署與執行平台（後端運行環境）
> 🔹 功能：在雲端穩定運行你設計的 Graph，支援擴展、容錯、記憶儲存與觀察（via LangSmith）

> **Run at scale with LangGraph Platform**
> Use LangGraph Platform’s APIs to design agent-driven user experiences
> featuring human-in-the-loop, multi-agent collaboration, conversation history,
> long-term memory, and time-travel. Deploy with fault-tolerant scalability.

🔗 *Learn more about LangGraph Platform*


| 項目      | 說明                                                     |
| ------- | ------------------------------------------------------ |
| 🌐 部署方式 | **SaaS 雲服務**（支援 CI/CD、自動化部署）                               |
| ⚙️ 特性   | 高可用（HA）、容錯（Fault-tolerant）、記憶體持久化、Human-in-the-loop 支援 |
| 🔍 整合工具 | 可與 **LangSmith** 整合，監控每個節點行為與輸入輸出內容                        |
| 📈 適用場景 | 金融、法務、醫療等需要穩定性、稽核性、高度可控的 LLM 應用                        |

---

## 🧭 整體對應關係圖

```
設計 →       開發 →           部署 →
LangGraph Studio → LangGraph Library → LangGraph Platform
（無代碼）       （程式碼）         （雲端執行）
```

---

## ✅ 使用建議

| 使用者角色            | 適合工具               |
| ---------------- | ------------------ |
| 資深工程師            | LangGraph Library  |
| 業務 / 設計師         | LangGraph Studio   |
| DevOps / AI 團隊部署 | LangGraph Platform |

---

- Focuses on **LangGraph** 的核心概念與實作 with **LangSmith** 監控。

### 何時以及如何使用框架
- https://www.anthropic.com/engineering/building-effective-agents

有許多框架可以使代理系統更易於實現，包括：

- LangChain 的LangGraph ；
- Amazon Bedrock 的AI Agent 框架；
- Rivet，一個拖放式 GUI LLM 工作流程建構器；
- Vellum，另一個用於建立和測試複雜工作流程的 GUI 工具。

*這些框架**簡化**了標準的**低階任務**，例如調用 LLM、定義和解析工具以及連結調用，從而簡化了入門流程。然而，它們通常會創建額外的抽象層，這可能會掩蓋底層的提示和回應，使其更難調試。此外，它們還可能讓人傾向於增加複雜性，而實際上**更簡單的設定**就足夠了。*

- 我們**建議開發者**從直接使用 LLM API 開始：許多模式只需幾行程式碼即可實現。
- 如果您確實**使用框架**，請確保您**了解底層程式碼**。對底層機制的錯誤假設是顧客常見的錯誤來源。

## 🧠 結論

這篇文章對 Agent Frameworks 的看法並非負面，而是：

- ✅ 強調：實用導向設計原則
- ⚠️ 警示：不要陷入架構設計主義（Architecture Astronaut）
- 🚀 鼓勵：先交付簡單可落地的功能，再逐步演化代理人能力

---

### **LangGraph** Terminology


**Agent Workflows** are represented as **graphs**

---

🔶 **State**（黃色）

> represents the current snapshot of the application.


🟠 **Nodes**（橘色）

> are python functions that represent agent logic.
> They receive the current **State** as input, do something, and return an updated **State**.

🔵 **Edges**（藍色）

> are python functions that determine which **Node** to execute next based on the **State**.  They can be **conditional** or fixed.

🟠 **Nodes** **do** the work.
🔵 **Edges** choose what to do **next**.

圖示內容（節點與連線）：

```
       Node
      /    \
Edge       Edge
  |         :
  |         :  
Node      Node

```

* 中央為一個 **Node**
* 左側透過實線 **Edge** 指向下一個 **Node**
* 右側透過虛線 **Edge** 指向另一個 **Node**

整體結構表示：狀態（State）流經節點（Node），由邊（Edge）決定下一步行為。這正是 LangGraph 的 agent 工作流程圖設計原則。

---

### **Five steps to the first Graph**

🔶 **1** - Define the **`State`** class 
⚪ **2** - Start the Graph Builder
🟠 **3** - Create a **`Node`**
🔵 **4** - Create **`Edges`**
⚫ **5** - Compile the Graph

---

### Example: Simple Graph - ✅ 五個步驟的 Python 程式碼示例

```python
from typing import TypedDict
from langgraph.graph import StateGraph

# 步驟 1：定義 State schema —— 用 TypedDict 或 dataclass / BaseModel 均可
class MyState(TypedDict):
    value: str
    count: int  # 加入計數欄位

# 步驟 2：啟動 Graph Builder
builder = StateGraph(MyState)

# 步驟 3：建立 Node —— 一定要「回傳 dict」！
def my_node(state: MyState) -> dict:
    print(f"[Node] Received state: {state['value']}, count: {state['count']}")
    return {
        "value": "processed",
        "count": state["count"] + 1
    }   # 回傳處理後狀態與遞增次數

builder.add_node("process", my_node)

# ★ 新增一個終止用的空節點
def end_node(state: MyState) -> dict:
    completed = "completed"  # 這裡可以是任何處理邏輯
    state["value"] = completed  # 明確改變 value
    print(f"[Node] Received state: {state['value']}, count: {state['count']}")
    return {
        "value": completed  # 明確改變 value
    }

builder.add_node("end", end_node)

# 步驟 4：Edge & 入口
def counter(state: MyState) -> str:
    # 若未達三次 → 回到 process；否則走向 end
    if state["count"] >= 3:
        return "end"
    else:
        return "process"

builder.set_entry_point("process")
# 指定 counter 以及「合法目的地」(process, end)
builder.add_conditional_edges("process", counter, ["process", "end"])

# 步驟 5：編譯並執行
app = builder.compile()
final_state: MyState = app.invoke({"value": "initial", "count": 0})
print("Final state:", final_state.get("value"), ", count:", final_state.get("count"))

```


## Week 4 Day 2

```cmd
py testLangGraph.py
```
---

### 🧠 說明

| 步驟      | 說明                        |
| ------- | ------------------------- |
| `State` | 保存應用狀態資料，例如輸入、過程中產生的中介資料等 |
| `Node`  | 執行實際的業務邏輯，對狀態進行變更         |
| `Edge`  | 決定流程從哪個節點移動到哪個節點，可以依條件決策  |
| `Graph` | 將 Node 與 Edge 組成完整工作流程圖   |

---

http://localhost:8888/lab/tree/4_langgraph/1_lab1.ipynb

## Week 4 Day 3

### 🕳️ **LangGraph Going Deeper** 

---

🟨 **📈 LangSmith**

🟧 **🧰 Tools - out of the box**
  
🟧 **🛠️ Tools - custom**

🟦 **📷 CheckPointing**

---

### **The `Super-Step`**

> 🟦 **"A super-step can be considered a single iteration over the graph nodes.
> Nodes that run in parallel are part of the same super-step,
> while nodes that run sequentially belong to separate super-steps."**

---

### 🧠 概念說明：

* 一個 **Graph** 通常描述一個 **Super-Step**。
* 每個 **Super-Step** 是一次代理人與工具間的互動，實現某個目的。

---

### 🟡 用法重點：

* 每次與使用者的互動都是一次新的：

  ```python
  graph.invoke(state)
  ```

---

### 📝 注意事項：

> *The reducer handles updating state **during** a super-step
> but **not between** super-steps.*

> ✅ **Reducer 僅會在同一個 Super-Step 中更新狀態，
> 不會在 Super-Step 之間傳遞狀態。**

---

### LangSmith 監控

https://smith.langchain.com/ => Sign up => Set up tracing => Generate API Key

```.env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="lsv2_pt_00b4d03b11b74931..."
LANGSMITH_PROJECT="pr-flowery-cloakroom-27"

```

http://localhost:8888/lab/tree/4_langgraph/2_lab2.ipynb

### ✅ **LangGraph 的 `thread_id` 和 `checkpoint_id`**

**LangGraph's `thread_id` and `checkpoint_id`** is designed specifically to support **branching, recovery, and multi-threaded conversational flows**. 

---

### Switching between `thread_id` 
```cmd
config = {"configurable": {"thread_id": "3"}}
# OR
config = {"configurable": {"thread_id": "2"}}
# OR
config = {"configurable": {"thread_id": "4"}}
```

### **Checkpointing**
Here is the **diagram transcription** with a text-based representation and explanation:

---

### 📌 **Checkpointing**

```text
┌──────────────┐
│ Define Graph │     ← Initialization step
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Super-step 1 │     ← First run of a set of graph nodes
└──────┬───────┘
       │           ⤷ 🧠 Checkpoint saved
       ▼
┌──────────────┐
│ Super-step 2 │     ← Next iteration of graph execution
└──────┬───────┘
       │           ⤷ 🧠 Checkpoint saved
       ▼
┌──────────────┐
│ Super-step 3 │     ← Another run, possibly branching or continuing
└──────────────┘
                ⤷ 🧠 Checkpoint saved
```

🧠 = Represents a snapshot of the graph’s state stored after each **super-step**.

---

### 💡 Key Concepts:

* **Define Graph**: Where you configure your nodes and flow.
* **Super-step**: One full execution round through the graph (may include parallel nodes).
* **Checkpoint**: A saved snapshot of the state at the end of each super-step.

  * Enables *branching*, *recovery*, or *auditability*.
  * Accessible by `checkpoint_id`.

---

## Week 4 Day 4 - Sidekick

### **Going Deeper**

🛠️ **Introducing a powerful tool**

🧱 **Structured outputs**

🔷 **Multi-agent workflow**

---

### Install Playwright

```cmd
uv pip install playwright
uv run playwright --version
  Version 1.52.0
uv run playwright install
```

http://localhost:8888/lab/tree/4_langgraph/3_lab3.ipynb

#### Sidekick
http://localhost:8888/lab/tree/4_langgraph/4_lab4.ipynb 

## Week 4 Day 5 - Sidekick with more tools

### Tools
🕸️ Searching the web  
📢 Sending notifications  
📁 Using the file system  
📚 Wikipedia  
💻 Python REPL

### 🧠 The Sidekick App

⚠️ Caution: use at your own risk!  
If you're not comfortable, then remove the PythonREPL and online navigation tools

🧱 It's a starting point that needs continued experiments and investigations

📂 But so much opportunity!

---

4_langgraph\sidekick_tools.py
4_langgraph\sidekick.py
4_langgraph\app.py

```cmd
cd 4_langgraph
py app.py
```
