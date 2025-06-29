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

* SK = code-centric orchestration for **LLM apps**.
* AutoGen = conversation-centric orchestration for **multi-agent systems**.

### 🪄 **What is AutoGen Core?**

- 🟨 An Agent **interaction** framework
  -  一個代理(Agent)互動框架 主要關注於如何讓不同的 AI 代理之間進行互動和溝通。
- 🟧 Agnostic to Agent **abstraction**
  - 不限制或規定代理應該如何被實現或定義。它對於代理的具體實現方式保持開放和靈活。
- 🔵 Somewhat similar positioning to **LangGraph**
  - 在某些方面可能與 LangGraph（另一個 AI 相關的工具或框架）有相似的功能或目標。

_But focus is on **managing interactions** between **distributed** and **diverse** Agents_

- AutoGen Core 是一個專注於 AI 代理之間互動的框架，它在設計上保持了靈活性，允許使用者根據自己的需求來定義和實現代理。 
- Using different programming paradigms, developers can create agents that best fit their specific use cases.

---

### 舉例說明 AutoGen Core 的特點:

1. 代理互動框架:
   假設您想創建一個自動化客戶服務系統。您可以使用 AutoGen Core 來設置**多個AI代理:**
   - 一個**接待員代理**來接收初始查詢
   - 一個專門處理**賬單問題代理**
   - 一個處理**技術支持代理**
   - 一個**管理員代理**來協調其他代理

   AutoGen Core 會幫助這些代理之間順暢地交互,例如接待員可以將賬單問題轉給**賬單代理**,或將技術問題轉給**技術支持代理**。

2. 對代理抽象化保持中立:
   - 您可以使用不同的AI模型來實現每個代理。例如,接待員可能使用GPT-3,賬單代理可能使用一個專門訓練的財務模型,技術支持代理可能結合使用一個**知識庫**和**BERT**模型。
   - AutoGen Core 不會限制您如何實現這些代理,它只關注於如何讓它們互相溝通。

3. 與 LangGraph 相似:
   就像 LangGraph 允許您創建語言處理流程一樣,AutoGen Core 允許您創建代理互動流程。例如:
   - 在 LangGraph 中,您可能創建一個流程來分析文本、提取關鍵詞、然後生成摘要。
   - 在 AutoGen Core 中,您可能創建一個流程,讓接待員代理接收查詢、**決定合適**的專門代理、將查詢轉發給該代理、然後將回答返回給用戶。

**AutoGen Core** 作為一個**靈活**的框架,幫助開發者創建**複雜的、多代理**的AI系統,而**不受限**於特定的**AI實現**方式。

```cmd
py testAutoGen3.py
```
---

### AG Fundamental principle

- It decouples an Agent's **logic** from how **messages are delivered**.
- The framework manages **creation** and **communication**.
- Agents are responsible for their **logic**, which is distinct from the Autogen Core.

---

### Two Types of Runtime

- Standalone (Day 3)
- Distributed (Day 4)

But only high level

_Goal: give you a flavor to see if this is relevant for you and worth further R&D_

---

http://localhost:8888/lab/tree/5_autogen/3_lab3_autogen_core.ipynb

```
py 3_lab3_autogen_core.py
```

## Week 5 Day 4

### AG Two Types of Runtime:

**Standalone** 
_**Distributed**_

- "Standalone yesterday, distributed today"
- "Even higher level"
- Goal: _give you a flavor to see if this is relevant for you and worth further **R&D**_

---

### “Distributed Runtime”（分布式运行时）的定义。主要内容包括：

- 一个**分布式代理（distributed agent）**负责生命周期管理和跨流程边界的通信。
  - **Host service**（宿主服务）：连接到worker runtimes，处理消息传递和会话管理。
  - **Worker runtime**（工作运行时）：向宿主服务广告代理（agents），并负责执行它们的代码。

---

### 关于分布式运行时（Distributed Runtime）的总结如下：

**分布式运行时**是AutoGen核心架构中的一个**更高级别**的概念，设计用于处理跨进程（甚至可能**跨不同平台和语言**）之间的消息传递和业务协调。它不像单线程版本那样局限于一台机器，而是可以在多个进程甚至多台设备上运行，增强了系统的扩展性和灵活性。

**分布式运行时**主要由两个部分组成：
- **Host Service（宿主服务）**：类似于一个容器，管理多个**Worker Runtime**。它负责消息的传输、会话管理和远程过程调用（例如**gRPC**），处理消息在不同计算节点间远距离传递的细节。
- **Worker Runtime（工作运行时）**：在每个节点上运行，管理实际的**代理（Agents）**，并与**宿主服务通信**。它维护自己的注册代理信息，并负责代理代码的执行。

目前，这一技术仍处于**实验阶段**，API可能会变动，还**不能直接用于生产环境**。但它代表了未来复杂分布式智能系统的架构方向，提供了在不同平台、多进程环境中实现代理协作的可能性。

多个Worker Runtime可以同时工作。这也是分布式架构的核心优势之一：

- **并行处理**：多个Worker Runtime可以并行处理不同的任务或在不同的机器上运行，极大提高系统的吞吐量和效率。
- **扩展性强**：随着需求增加，可以增加更多的Worker Runtime来应对更大量的任务，无需更改核心架构。
- **高可用性**：其中某个Worker Runtime出现故障，其他的仍在运行，可以保证系统的持续工作。
- **协作操作**：多个Worker Runtime通过宿主服务协调，进行任务分配、消息传递，实现整个平台的整体工作。

_总结：**多个Worker Runtime可以同时运行并协作**，这是分布式系统提升性能和弹性的关键。_

---

http://localhost:8888/lab/tree/5_autogen/4_lab4_autogen_distributed.ipynb

```cmd
py 4_lab4_autogen_distributed.py
```
