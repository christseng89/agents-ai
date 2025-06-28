# Week 5 - Microsoft AutoGen Framework

## Week 5 Day 1
### **AutoGen** `AG` 

<span style="color:gold">AutoGen 0.4 released January 2025</span>

<span style="color:orangered"><i><b>from-the-ground-up rewrite</b> adopting an asynchronous, event-driven architecture to address issues such as observability, flexibility, interactive control, and scale.</i></span>


<span style="color:deepskyblue"><b>It is a replacement for AutoGen 0.2</b></span>

---

### **AutoGen DRAMA**

<span style="color:gold">Several of the original developers of AutoGen left Microsoft and split off in late 2024 to create a <b>fork of AutoGen</b></span>

<span style="color:chocolate">Called AG2 or AgentOS 2, compatible with earlier AutoGen 0.2</span>

<span style="color:deepskyblue"><b>If you pip install autogen, you get AG2!</b></span>

---

### **Microsoft AutoGen** `AG` Modules

- 🟦 **AutoGen Core** *(V)*
*Event-driven framework for scalable multi-agent AI systems*

- 🟧 **AutoGen AgentChat** *(VV)*
*Conversational Single and Multi-Agent Applications*

- 🟫 **AutoGen Studio**
*Low-code / No code app*

- 🟫 **AutoGen CLI** _(Magentic One CLI)_
*A console-based assistant*

---

### **AG Core Concepts**

* 🧠 **Models** `🟡`

  > 提供語言生成能力的基礎，如 GPT-4、GPT-3.5 等。

* 💬 **Messages** `🟧`

  > Agents 之間溝通的訊息結構，支持角色、內容、格式等控制。

* 🤖 **Agents** `🟦`

  > 執行任務的實體，能回應訊息、執行工具、協同合作。

* 👥 **Teams** `⚪`

  > Agent 的組合，支援協作與任務分工。

---

https://github.com/microsoft/autogen

```cmd
py testAutoGen1.py
py testAutoGen2.py

```
http://localhost:8888/lab/tree/5_autogen/1_lab1_autogen_agentchat.ipynb

## Week 5 Day 2

### 🅰️🌀  **Going Deeper**

🕶️  **Multi-modal**              

🟧 **Structured Outputs**

🔧  **Tools from LangChain**     

👥 **Teams**

❓  **And special guest** (MCP Server)

---

http://localhost:8888/lab/tree/5_autogen/2_lab2_autogen_agentchat.ipynb


## Week 5 Day 3

### 🅰️🌀  **AutoGen AgentChat** vs **SK**
---

#### ✅ **Microsoft Semantic Kernel (SK)**

**→ An SDK for building AI “agents” or apps with structured logic and skills.**

🔹 **Purpose:**

* A developer framework for connecting LLMs to real-world code, APIs, tools, and memory.

🔹 **Key Features:**

* Plugins / skills (wrap functions or prompts)
* Planning & orchestration
* Memory (embeddings, semantic search, chat history)
* Integrates with C#, Python, Java
* Works with any LLM (OpenAI, Azure OpenAI, local models)

🔹 **Use cases:**
✅ Chatbots that can call APIs
✅ Agents performing multi-step workflows
✅ Summarization apps
✅ RAG pipelines
✅ Business logic + LLM orchestration

---

#### ✅ **Microsoft AutoGen**

**→ A high-level framework for multi-agent collaboration.**

🔹 **Purpose:**

* A research-driven system for coordinating multiple AI agents that talk to each other to solve a task.

🔹 **Key Features:**

* Agents as objects (AssistantAgent, UserProxyAgent, etc.)
* Agents converse in natural language
* Round-robin or custom conversation logic
* Supports asynchronous conversations
* Good for **multi-agent systems** (e.g. “agent teams”)
* Allows tools (plugins) for agents
* Integrates with OpenAI, Azure OpenAI, and LangChain tools

🔹 **Use cases:**
✅ Multi-agent systems where different agents have roles
✅ Scenarios where agents reason collaboratively
✅ Teaching LLMs to reflect on their actions
✅ Complex “agent societies” (e.g. research assistants working together)

---

#### 🚀 **The Core Difference**

| **Feature**              | **Semantic Kernel**                | **AutoGen**                       |
| ------------------------ | ---------------------------------- | --------------------------------- |
| Main purpose             | Orchestrate **LLM** + skills/functions | Build **multi-agent** conversations   |
| Programming model        | Skills, planners, plugins          | Agents chatting back and forth    |
| Language of coordination | Code + functions + planners        | Natural language between agents   |
| Conversation model       | Typically **single-agent + tools**     | **Multi-agent chat loop**             |
| Memory / context         | Semantic memory, vector stores     | Conversation history in messages  |
| Developer audience       | App developers, AI integration     | AI researchers, experimental devs |

---

#### 🎯 Example Scenarios

**Using Semantic Kernel:**

> “Build me a bot that reads PDFs, summarizes them, and stores results in a vector store.”

✅ SK is perfect.

* Plug in PDF reading as a skill.
* Add semantic memory.
* Call OpenAI to summarize text.

---

**Using AutoGen:**

> “Have two agents—one to find flights, one to compare prices—debate which is better and give me a final recommendation.”

✅ AutoGen is perfect.

* Create two agents with separate responsibilities.
* Let them talk back and forth in natural language.
* User proxy agent observes or steers conversation.

---

#### 💡 Analogy

* **Semantic Kernel** is like:

  > “An **SDK** for wiring up **LLMs** into structured software apps.”

* **AutoGen** is like:

  > “A lab where multiple LLM **agents** hold a conversation to solve problems together.”

They overlap a bit—for example, both can wrap tools—but they come from different design philosophies:

* SK = deterministic, structured pipelines
* AutoGen = emergent behavior from conversation

---

#### ✅ When to Choose Which?

| **Scenario**                                   | **Recommended** |
| ---------------------------------------------- | --------------- |
| Chatbots with tools and memory                 | Semantic Kernel |
| Single-agent apps that integrate APIs          | Semantic Kernel |
| Multi-agent conversations with defined roles   | AutoGen         |
| Experimental multi-LLM reasoning               | AutoGen         |
| Production software needing deterministic flow | Semantic Kernel |
| Prototyping collaborative agents               | AutoGen         |

---

Both are powerful and **can be combined**:
✅ For example, an agent in AutoGen could internally use Semantic Kernel skills for precise tasks!

---

**TL;DR**

* SK = code-centric orchestration for **LLM apps**.
* AutoGen = conversation-centric orchestration for **multi-agent systems**.

### 🪄 **What is AutoGen Core?**

🟨 An Agent **interaction** framework
🟧 Agnostic to Agent **abstraction**
🔵 Somewhat similar positioning to **LangGraph**

_But focus is on **managing interactions** between **distributed** and **diverse** Agents_

---
