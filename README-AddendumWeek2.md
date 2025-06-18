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
- 3️⃣ **Call** `await Runner.run()` **to run the agent**

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

## Week 2 Day 2

---

### **Automated Sales Outreach**

**We will build:**

- 📝 **A workflow of Agent calls**
- 🔧 **An agent that can use a tool**
- 📊 **An agent that can call on other agents**
    - 🔁 **Tools vs Handoffs**

---

### SendGrid - Sending Emails

- https://sendgrid.com/
- https://app.sendgrid.com/guide => Settings => API Keys 
    - Name: Agents-AI
    - Permissions: Full Access
    - Create Key

2_openai/2_lab2.ipynb

## Week 2 Day 3
### **Recap – Day2 - 3 interactions**

* 🛠️ **Tools**
* 🧰 **Agents as Tools**
* 🤝 **Handoffs**

---

**Adding to the mix**

* 👥 **Models other than OpenAI**
* 🧱 **Structured Outputs**
* 🚆 **Guardrails**

---

### Guardrails

A **guardrail** in Agent AI is a **rule or constraint** that ensures the agent behaves safely and predictably. It can:

* **Validate inputs** (e.g., block names or PII)
* **Limit tool use** (e.g., restrict sending emails)
* **Control outputs** (e.g., remove unsafe content)
* **Stop loops or errors** (e.g., max 5 turns)

It’s like a **safety filter** around the agent's actions.

---

2_openai/3_lab3.ipynb

## Week 2 Day 4
### Deep Research
- **Deep Research** is a technique where an agent uses other agents to gather information.
- It’s like a **team of agents** working together to solve a problem.
- **Example**: An agent that finds the best restaurant by asking other agents for reviews, menus, and prices.

### Using Tools, Structured Outputs and Hosted Tools

### OpenAI Hosted Tools

OpenAI Agents SDK includes the following **Hosted Tools**:

- The `WebSearchTool` lets an agent search the web.  
- The `FileSearchTool` allows retrieving information from your OpenAI Vector Stores.  
- The `ComputerTool` allows automating computer use tasks like taking screenshots and clicking.

```code
SEARCH_INSTRUCTIONS = "You are a research assistant. Given a search ... return a summary of the top results."

search_agent = Agent(
    name="Search Agent",
    instructions=SEARCH_INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size="low")],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)
```

2_openai/4_lab4.ipynb

```note
# HOW_MANY_SEARCHES = 3 # Start from 3 searches to Test
HOW_MANY_SEARCHES = 10 # Final run with 10 searches
```

## Week 2 Day 5

### Essential use-case: Deep Research
- Now as a python application, featuring Gradio

2_openai/deep_research/deep_research.py

```cmd
cd 2_openai\deep_research
py deep_research.py
   - What are some of the most exciting commercial applications of Autonomous Agentic AI as of June 2025?
   - What are some of the most exciting commercial applications of Autonomous Agentic AI for Financial Institutions as of June 2025?
   - Latest AI Agent frameworks in 2025
```

### And now, the big challenge
- Start by coming up with 3 clarifying questions based on the query
- Tune the searches taking into account the clarifications
- Make the Manager an Agent with agents-as-tools and handoffs

#### Deploy deep_research.py to Hugging Face Spaces

```notes
# Add files
app.py
requirements.txt
deep_research\__init__.py

revise code to use 'deep_research.'
- deep_research\deep_research.py
- deep_research\research_manager.py
```

```cmd
cd ..
py app.py

uv run gradio deploy

```

### 📦uv run gradio deploy Work Through
Creating new Spaces Repo in 'D:\development\agents-ai\2_openai'. Collecting metadata, press Enter to accept default 
value.
Enter Spaces app title [2_openai]: **DEEP RESEARCH**
Formatted to DEEP_RESEARCH. 
Enter Gradio app file : **app.py**
Enter Spaces hardware (cpu-basic, cpu-upgrade, cpu-xl, zero-a10g, t4-small, t4-medium, l4x1, l4x4, l40sx1, l40sx4, l40sx8, a10g-small, a10g-large, a10g-largex2, a10g-largex4, a100-large, h100, h100x8) [cpu-basic]:
Any Spaces secrets (y/n) [n]: **y**
Enter secret name (leave blank to end): **OPENAI_API_KEY**
Enter secret value for OPENAI_API_KEY: **sk-proj-ypFvL65Ev...**
Enter secret name (leave blank to end): **SENDGRID_API_KEY**
Enter secret value for SENDGRID_API_KEY: **SG.QXJhafDnStuLg...**
Enter secret name (leave blank to end):
Create Github Action to automatically update Space on 'git push'? [n]: **n**
Space available at https://huggingface.co/spaces/christseng898/DEEP_RESEARCH

#### Special Notes:
- **README.md** will be created in the folder 2_openai after deploy.

- https://huggingface.co/spaces/christseng898/DEEP_RESEARCH
