# Week 6 - MCP
- MCP only works in **WSL**

## Week 6 Day 1
### “如果你刚加入我们...” 
- 很着急学习最先进的能力 **(MCP)**！”  

- **课程内容安排：**  
  - **第一周（Week 1）**：专注于“原生API与工具的直接使用”。强调基础、原始的能力。  
  - **第二周（Week 2）**：学习“OpenAI代理SDK”，代表更高级、更封装的开发工具。

### MCP (Model Context Protocol) was proposed by OpenAI.

### **What it’s not** *(orange)*

🟧 A **framework** for building **Agents**

🟧 A fundamental change to how **Agents** work

🟧 A way to code **Agents**


### **What it is** *(yellow)*

🟨 A protocol **standard**

🟨 A simple way to integrate **tools, resources, prompts**

🟨 A **USB-C port** for AI applications

---

### MCP

#### **Reasons not to be excited** *(orange)*

🟧 It’s just a **standard**, it’s **not tools** themselves

🟧 LangChain already has a **big Tools ecosystem**

🟧 You can already make any function into a **Tool**


#### **Reasons to be excited** *(yellow)*

🟨 Makes it frictionless to **integrate**

🟨 It’s taking off! **Exploding ecosystem**

🟨 **HTML** was just a standard, too 😉

---

### MCP Core Concepts

#### **The Three Components:**

🔵 **Host** is an LLM app like Claude or our **Agent** architecture

🟨 **MCP Client** lives inside Host and connects 1:1 to MCP Server

🟧 **MCP Server** provides tools, context and prompts

#### **Example:**

- Fetch is an 🟧 **MCP Server** that searches the web via a headless browser
- You can configure 🔵 **Claude Desktop** (the host) to run an 🟨 **MCP Client** that then launches the Fetch MCP Server on your computer
- We did that last week with AutoGen
---

#### MCP Core Concepts (continued)
→ **Host** 内嵌了 **MCP Client**，
→ MCP Client 会连接到 **MCP Server**，
→ 从 MCP Server 获取各种服务、工具、上下文或提示词。

因此，Host 就像“使用者”，而 MCP Server 则提供背后的功能支持。

---

**Agent** 也可以使用 **MCP Client** 去连接 **MCP Server** 并获得服务。

* Agent 通常是一个基于大语言模型（LLM）或其他 AI 逻辑构建的软件程序。
* 在 Agent 内部，可以嵌入 **MCP Client**。
* MCP Client 会与 **MCP Server** 通信，获取工具、资源或上下文信息。

因此，不仅像 Claude 这样的 Host 能用 MCP，**任何 Agent** 也都可以通过 MCP Client 来使用 MCP Server 提供的服务。

---

### ✅ *MCP Architecture Diagram**

```
+===============================================================+
|                         Your Computer                         |
|                                                               |
|   +-------------------------------------------------------+   |
|   |                       HOST                           |    |
|   |                                                      |    |
|   |   +-------------------+   +----------------------+   |    |
|   |   |    MCP Client     |   |     MCP Client       |   |    |
|   |   +-------------------+   +----------------------+   |    |
|   |                    |                   |             |    |
|   |                    |                   |             |    |
|   |   +-------------------+                |             |    |
|   |   |    MCP Client     |                |             |    |
|   |   +-------------------+                |             |    |
|   +----------------------------------------|-------------+    |
|         |              |                   |                  |
|         |              |       +===========|==================+            
|         v              v       |           v             
|   +----------+   +----------+  |  +---------------+      
|   | MCP      |   | MCP      |  |  | MCP Server    |      
|   | Server   |   | Server   |  |  | (Remote, rare)|      
|   +----------+   +----------+  |  +---------------+      
|        |               |       |           |             
|        |               |       |           |             
|        v               v       |           v             
|  +-----------+   +-----------+ |   +-------------+      
|  | Local FS  |   | Web APIs  | |   | Remote API  |      
|  | or tools  |   | or online | |   | or services |      
|  +-----------+   +-----------+ |   +-------------+      
+================================+

```

---

#### ✅ Explanation

* **HOST**

  * Runs on your computer.
  * Could be Claude Desktop, Autogen, or your custom agent framework.
  * Hosts multiple MCP Clients.

* **MCP Clients**

  * Tiny “plugin-like” processes inside the host.
  * Each connects **1-to-1** with an MCP Server.
  * Several clients may exist in the host, each serving different tools.

* **Local MCP Servers**

  * Run **outside** the host but still on your machine.
  * Provide tools, context, or prompts.
  * Examples:

    * Local file system readers.
    * Fetch server running headless browser with Playwright.

* **Remote MCP Servers (rare)**

  * Run on remote machines.
  * Require SSE (Server-Sent Events) transport.
  * Used only when the MCP server itself is hosted externally.

* **External APIs**

  * Local MCP Servers may call out to external APIs (e.g. weather, web scraping).
  * This happens **from the local MCP server**, not directly from the host.

---

**Two "Transport" mechanisms**
- *Stdio spawns a process and communicates via standard input/output*
- *..while SSE uses **HTTPS** connections with streaming*

---
#### ✅ Key Insights 

* Most MCP servers **run locally on your box**.
* Remote MCP servers exist but are rare.
* **Transport** methods:
  * Local → can use STDIO (most common) or SSE.
  * Remote → must use SSE.
* MCP clients live inside the host and talk to MCP servers.
* MCP servers can wrap external APIs as “tools.”

---

http://127.0.0.1:8888/lab/tree/6_mcp/1_lab1.ipynb

**Note:**
- Create `sandbox` subfolder in folder `6_mcp`.

```cmd
cd 6_mcp
uv run 1_lab1.py
```

### MCP Marketplace

- https://huggingface.co/blog/LLMhacker/top-11-essential-mcp-libraries **Top 11**
- https://mcp.so/ **Top #1**
- https://smithery.ai/ **Test MCP Server** 
- https://huggingface.co/blog/Kseniase/mcp **An interesting topics**

**Security** is a concern to use **MCP Servers**, so be careful with MCP servers you run.  Get the big companies' MCP servers, like OpenAI, Microsoft, etc.

## Week 6 Day 2 - building an owned MCP Server

### ✅ MCP Core Concepts

#### **The 3 Components:**

* 🟦 **Host**
  is an LLM app like Claude or our Agent architecture

* 🟨 **MCP Client**
  lives inside Host and connects 1:1 to MCP Server

* 🟧 **MCP Server**
  provides tools, context and prompts

#### **Example:**

* **Fetcher** is an 🟧 **MCP Server** that searches the web via a headless browser.

* You can configure 🟦 **Claude Desktop** (the host) to run an 🟨 **MCP Client** that then launches the **Fetcher MCP Server** on your computer.

> We did that last week with AutoGen.

---

Fantastic! Let’s convert the slide’s text **and** diagram contents into structured text, preserving colors and symbols for clarity.

---

#### ✅ MCP Architecture Overview

🚀 **Usage Scenarios**

* **Local Only (File Writer)**

  * MCP Client ↔ **STDIO** ↔ MCP Server on your machine.

* **Local Server → Remote API**

  * MCP Client ↔ **STDIO** ↔ MCP Server ↔ **Remote** API calls.

* **Fully Remote (Managed/Hosted)**

  * MCP Client ↔ **SSE** ↔ **Remote** MCP Server **(rare)**.

---

### **⚙️ Making an MCP Server**

#### **🟧 Why make an MCP Server**

- 🟠 Allow **others** to incorporate tools and resources
- 🟠 **Consistently** incorporate all our MCP Servers
- 🟠 Understand the **plumbing**

---

#### **🟨 Reasons not to make an MCP Server**

- 🟡 *If it’s an **internal use** only, then we could just make tools —*the `@function_tool` decorator can make any function into a tool*

### **🟨 But...When using MCP Server**

✅ Even internal users should often **call an external MCP server** because:

* isolates sensitive data logic
* centralizes **authentication** and **authorization**
* enables **logging** and **audit trails**
* enforces **Zero Trust** principles
* future-proofs **external integrations**


> _“Even for **internal users**, using an **external** MCP server is safer.”_

---

http://127.0.0.1:8888/lab/tree/6_mcp/2_lab2.ipynb

```cmd
cd 6_mcp
uv run accounts.py
uv run 2_lab2.py
uv run app.py
```

#### Special Note
**accounts.py** was written by CrewAI in Week 4 with a new **database.py** using Sqlite database.

#### Exercise

```
cd 6_mcp
cd 6_mcp/exercise_date
uv run openai_date_tool.py
  LLM calls function: 'get_today_date'
  [07/01/25 18:31:52] INFO     Processing request of type CallToolRequest                                    server.py:556
  Today's date is July 1, 2025.

cd ..
```

## Week 6 Day 3 - MCP Server (internal & external)

```cmd
npm install mcp-memory-libsql
```

### Remote MCP servers (SSE)
https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers

### Build a SSE Remote MCP Server
https://developers.cloudflare.com/agents/guides/remote-mcp-server/

```
cd 6_mcp
uv run 3_lab3.py
uv run 3_lab31.py
  market_server.py
  market.py
```

http://127.0.0.1:8888/lab/tree/6_mcp/3_lab3.ipynb
https://polygon.io/
 - Password: t0nnn$Xxxxx

## Week 6 Day 4


### 🎓 **CAPSTONE PROJECT!** - Autonomous Traders

💼 Commercial

🛠️ **5** MCP servers with tools and resources

🤝 Agent interactions

🔄 Autonomous

⚠️ **DO NOT** use for trading decisions!

---

```cmd
uvx mcp-server-fetch
npx @playwright/mcp@latest

export BRAVE_API_KEY=BSAl...
export POLYGON_API_KEY=RbyC...

npx -y @modelcontextprotocol/server-brave-search
uvx --from git+https://github.com/polygon-io/mcp_polygon@v0.1.0 mcp_polygon
```

### Special Note
- Using external Researcher MCP servers for tools
- Using owner Trader MCP servers for trading

```python
trader = Agent(
    name=agent_name,
    instructions=instructions,
    tools=[researcher_tool],  # 👈 Use Researcher as a tool
    mcp_servers=trader_mcp_servers,  # 👈 Use Trader MCP servers only
    model="gpt-4o-mini",
)
```

```cmd
cd 6_mcp
uv run 4_lab4.py
```

### Other files in this folder
- accounts.py => Handles accounts and database interactions
- app.py => Main application to run the MCP server
- database.py => Database interactions using Sqlite
- market.py => Market data retrieval and processing
- market_server.py => MCP server for market data
- mcp_params.py => Parameters for MCP servers
- templates.py => Best practices to use templates for prompts and instructions
- trader.py => Trader class to handle trading logic

http://127.0.0.1:8888/lab/tree/6_mcp/4_lab4.ipynb

## Week 6 Day 5 - MCP Server (internal & external)

### **Adding a few details**

🐮 The Trading Floor
👐 **Autonomy** to evolve strategy
👥 More Models
🖥️ A User Interface (gr)

---

### Tracer for OpenAI Agent SDK
- tracers.py 

### Update .env file
```note
GROK_API_KEY=xai-TRkI9oJ... # from console.x.ai
RUN_EVERY_N_MINUTES=60
RUN_EVEN_WHEN_MARKET_IS_CLOSED=True
USE_MANY_MODELS=True
```

- trading_floor.py
  - **asyncio.gather** to run multiple tasks concurrently
```cmd
cd 6_mcp
uv run app.py
uv run trading_floor.py
```

### 🎲 **Which Framework to select?**

✨ *It's not the most important question and it doesn't really matter!*

🤝 *Pick the framework that suits your style and the skills of your team*

🔥 *My go-to is **OpenAI Agents SDK + MCP**, but some prefer batteries included*

*We didn't cover some favorite frameworks like **Google ADK**, **HuggingFace SmolAgents** and **Pydantic AI** - but they will seem so familiar!*

---

### **What matters**

1. Start with the **problem**, not the solution
2. Have a **metric** to evaluate success
3. Favor **workflow** over autonomy initially
4. Work **bottom up**, not top down
5. Start **simple**, then add
6. Start with **large frontier models**, then reduce
7. Think **context** rather than memory
8. Most problems are solved with **prompts**
9. Look at the **traces**
10. Be a **scientist**; no shortcut to R&D

---
**Agentic AI 项目实战指南**

主要重点：

✅ 不要一上来就说「我要用 agent 做 X」——先搞清楚问题是什么。
✅ 为你的问题定义可衡量的 metric，并确保你有数据去测量它。
✅ 一开始先做简单的工作流，不要急着做全自主。
✅ 从 bottom-up 做起，小步快跑。
✅ 用高端模型先跑通，再考虑用轻量模型优化成本。
✅ 所有记忆机制的本质都是把对的 context 塞进 prompt。
✅ 遇到问题，先从优化 prompt 着手。
✅ 一定要看 trace，找隐藏的问题。
✅ AI 工程师要有科学家的心态，不断做实验、验证，不要只凭直觉。(no shortcuts to R&D)

这是一套非常实用的 **Agentic AI 项目实战指南**，特别适合正在投入 LLM / Agents 开发的团队。

---

## Recap from Week 1 to Week 6
非常好！以下是你圖片中的課程內容，**倒序排列**（從 Week 1 → Week 6）：

---

### **Week 1: Foundations**

* Understand Agentic Workflow
* Agents and Patterns
* Orchestrating LLMs
* Autonomy and Tools
* Project 1: Your personal career agent

---

### **Week 2: OpenAI Agents SDK**

* Understand OpenAI Agents SDK concepts
* Project 2: an SDR
* Tools vs Agents Guardrails
* Project 3: Deep Research
* Project 3: Deep Research app

---

### **Week 3: CrewAI**

* Understand CrewAI Concepts
* Build a Crew Agent
* Project 4: Stock Picker
* Project 5: Developer Agent
* Project 5: Engineering Team

---

### **Week 4: LangGraph**

* Understand LangGraph concepts
* Build a LangGraph Agent
* Tools, memory, web searches
* Project 6: Sidekick
* Project 5: Sidekick improvements

---

### **Week 5: AutoGen**

* Understand AutoGen concepts
* AutoGen Agent Chat
* AutoGen Core
* AutoGen Core - distributed
* Project 7: Agent Creator

---

### **Week 6: MCP**

* Agentic Architecture and MCP
* Building an MCP Server and Client
* Multiple Local and Remote MCP servers
* Project 8: AI Equity Traders
* Project 8: AI Equity Traders In Action

---
