# Week 6 - MCP
- MCP only works in WSL

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
