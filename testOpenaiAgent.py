# pip install --upgrade openai-agents openai-agents-tools requests
# 並在環境變數中 export/set OPENAI_API_KEY=<你的金鑰>
# 再 export/set PUSHOVER_USER=<你的 Pushover user key>
#    export/set PUSHOVER_TOKEN=<你的 Pushover app token>

import os          # NEW: required by push_notification
import requests    # NEW: required by push_notification

from agents import Agent, Runner, WebSearchTool, function_tool

# 1️⃣ 建立自訂計算器工具 -------------------------------------------------
@function_tool                 # 也可寫成 @tool
def calculator(expression: str) -> str:
    """Evaluate a math expression and return the result as string."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


# 2️⃣  PushOver notification tool ---------------------------------------
@function_tool
def push_notification(message: str) -> str:
    """Send a push notification via the Pushover API."""
    user  = os.getenv("PUSHOVER_USER")
    token = os.getenv("PUSHOVER_TOKEN")
    if not user or not token:
        return "Error: PUSHOVER_USER or PUSHOVER_TOKEN not set."

    print(f"Sending PushOver notification: {message}")  # 方便在 console 觀察
    try:
        resp = requests.post(
            "https://api.pushover.net/1/messages.json",
            data={"user": user, "token": token, "message": message},
            timeout=10,
        )
        resp.raise_for_status()
        return "Notification sent ✔"
    except Exception as e:
        return f"PushOver error: {e}"


# 3️⃣ 準備工具清單（內建 + 自訂）----------------------------------------
tools = [
    WebSearchTool(),           # 內建即時網頁搜尋
    calculator,                # 自訂 FunctionTool
    push_notification          # 自訂 PushOver 通知工具
]

# 3️⃣ 建立 Agent --------------------------------------------------------
agent = Agent(
    name="Assistant",
    instructions=(
        "You are a helpful assistant. "
        "After producing your final answer, ALWAYS call the push_notification tool "
        "with a concise (≤30-word) summary before you answer the user."
    ),
    tools=tools,
)

# 4️⃣ 執行並列印 --------------------------------------------------------
if __name__ == "__main__":
    res = Runner.run_sync(agent, "What's the capital of Mongolia?")
    print("LLM reply →", res.final_output)

    res = Runner.run_sync(agent, "3721 乘以 84 加 1 是多少？")
    print("LLM reply →", res.final_output)
