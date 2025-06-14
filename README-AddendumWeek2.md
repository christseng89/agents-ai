# Week 2 - OpenAI Agents SDK

## Week 2 Day 1

### Python Async Programming - asyncio
- *This is a very important topic!*

- *All the Agent Frameworks use* **asynchronous python**
*You can get by ignoring it but it will always* **bother you slightly**
- *Bite the bullet! Spend 30 minutes on the guide –* **you will thank me!**

### **The short version**

*All your methods and functions start* **async**
*Anytime you call them, use* **await**

```python
async def do_some_processing() -> str:
    # Do some work
    return "done!"

result = await do_some_processing()
```

### **The long version**

- **Asyncio** provides a lightweight alternative to threading or multiprocessing
- Functions defined with **async def** are called **coroutines** — they’re special functions that can be paused and resume
- Calling a **coroutine** doesn’t execute it immediately — it returns a coroutine object
- To actually run a coroutine, you must **await** it, which schedules it for execution within an **event loop**
- While a **coroutine** is waiting (e.g. for I/O), the **event loop** can run other coroutines

### **Richer examples**

```python
async def do_some_processing() -> str:
    # Do some work
    return "done!"

# running the function returns a coroutine
my_coroutine = do_some_processing()

# awaiting the coroutine returns a result
my_result = await my_coroutine
```

```python
results = await asyncio.gather(
    do_some_processing(),
    do_other_processing(),
    do_yet_more_processing()
)
```

### ✅ What it does:

* Runs all three coroutine functions **concurrently** using **`asyncio.gather`**.
* Waits for **all** of them to complete.
* Stores the return values in the `results` list.

---

### **Introducing OpenAI Agents SDK**

- **Lightweight and flexible**
- **Stays out of the way**
- **Makes common activities easy**
- **My favorite**

---

### **OpenAI Agents SDK - Minimal terminology**

🤖 **Agents** represent LLMs
🤝 **Handoffs** represent interactions
🚆 **Guardrails** represent controls

---

### **Three steps**

- 1️⃣ **Create an instance of** `Agent`
- 2️⃣ **Use** `with trace()` **to track the agent**
- 3️⃣ **Call** `await runner.run()` **to run the agent**

---

### ✅ Full minimal example:

```python
import asyncio
from openai import Assistant, runner

async def main():
    agent = Assistant(name="MyAgent")
    async with runner.trace(agent):
        await runner.run()

asyncio.run(main())
```
---

### Vibe Coding

- **Good vibes** – prompt well – ask for short answers and latest APIs for today's date
    **良好的感覺** – 撰寫良好的提示語 – 要求簡潔答案並使用最新的 API（註明今天日期）

- **Vibe but verify** – ask 2 LLMs the same question
    **感覺可以，但要驗證** – 問兩個 LLM 相同的問題

- **Step up the vibe** – ask to break down your request into independently testable steps
    **Setup vibe** – 將請求任務拆分為可獨立測試的步驟

- **Vibe and validate** – ask an LLM then get another LLM to check
    **感覺之後要驗證** – 問一個 LLM，然後請另一個 LLM 幫你檢查

- **Vibe with variety** – ask for 3 solutions to the same problem, pick the best
    **多樣 vibe** – 要求同一問題提供三種解法，選擇最佳方案

---

2_openai/1_lab1.ipynb
https://platform.openai.com/traces
