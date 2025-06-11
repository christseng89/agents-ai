# Agents AI

## Week 1 Day 1

### Startup
Flexible AI workflow automation https://n8n.io/

- **n8n.io** is a **low-code/no-code** workflow automation platform that allows users to create workflows by orchestrating between different applications without needing extensive coding knowledge.

### Week 1 to Week 6 learning roadmap:

* **🟤 Dark Coffee = Theory/Concepts**
* **🔵 Blue = Frameworks/Hands-on Implementations**
* **🟡 Gold = Projects/Applied Use Cases**

---

### ✅ **Week 1: Foundations**

🟤 Make an Agentic Workflow
🟤 Agents and Agentic Patterns
🟤 Orchestrating LLMs
🟤 Autonomy and Tools
🟡 **Project 1:** Your Personal Career Agent

---

### ✅ **Week 2: OpenAI Agents SDK**

🟤 Understand **OpenAI Agents SDK** Concepts
🟡 **Project 2:** an SDR
🔵 Tools vs Agents Guardrails
🟡 **Project 3:** Deep Research
🟡 **Project 3:** Deep Research App

---

### ✅ **Week 3: CrewAI**

🟤 Understand **Crew AI** Concepts
🔵 Build a Crew Agent
🟡 **Project 4:** Stock Picker
🟡 **Project 5:** Developer Agent
🟡 **Project 5:** Engineering Team

---

### ✅ **Week 4: LangGraph**

🟤 Understand **LangGraph** Concepts
🔵 Build a LangGraph Agent
🔵 Tools, Memory, Web Searches
🟡 **Project 6:** Sidekick
🟡 **Project 6:** Sidekick Improvements

---

### ✅ **Week 5: AutoGen**

🟤 Understand **AutoGen** Concepts
🔵 AutoGen Agent Chat
🔵 AutoGen Core
🔵 AutoGen Core - Distributed
🟡 **Project 7:** Agent Creator

---

### ✅ **Week 6: MCP (Multi-Agent Control Protocol)**

🟤 Agentic Architecture and MCP
🔵 Building an MCP Server and Client
🔵 Multiple Local and Remote MCP Servers
🟡 **Project 8:** AI Equity Traders
🟡 **Project 8:** AI Equity Traders in Action

---

This format visually distinguishes **what you’re learning (theory), how you’re building (frameworks), and where you’re applying it (projects)**—making it easier to track your progression from understanding to implementation to real-world use.

Based on your provided transcript and image, here’s a **summary of Projects 5 through 8** along with their significance, tone, and learning objectives:

---

### 🟡 **Project 5: Engineering Team** 工程團隊模擬器

> **"An agentic platform representing a real engineering team."**
「模擬一個真實軟體開發團隊的代理人平台」

* Simulates collaboration between agents playing specific engineering roles:

  * Frontend Developer
  * Backend Developer
  * Engineering Lead
  * Tester
* These agents **collaborate to build real software**, like a functioning backend system.
* **Learning focus:** how to model **role-based autonomy** and **multi-agent collaboration** for real-world engineering use cases.
* **Real twist:** The platform built by this team is reused in Project 8’s financial simulation.

---

### 🟡 **Project 6: Sidekick** 側邊助手

> **"A browser-controlling co-pilot agent on your desktop."**
「能與你一起在桌面上互動的 AI 瀏覽器副駕駛」

* This agent runs **alongside you**, with **interactive control over your browser**.
* Inspired by Chinese platform **Manus**, but unlike cloud-based agents, this one runs locally.
* You can **co-browse, automate clicks, scrape, search, and interact** with websites.
* **Learning focus:** real-time agent interaction and shared control — building an **AI copilot** you can work with side by side.

---

### 🟡 **Project 7: Agent Creator** 代理人生成器

> **"An agent that generates agents."**
「會自己產生代理人的代理人」

* You build a **meta-agent**, an agentic framework that can **spawn new agents**.
* These generated agents will perform commercial tasks.
* Not heavily commercial itself, but **highly educational and intellectually rich**.
* **Learning focus:** recursive agent design, self-generating frameworks, and tooling automation.

---

### 🟡 **Project 8: AI Equity Traders** AI 股市交易員

> **"Capstone: autonomous agents that trade in financial markets."**
「壓軸專案：金融市場的多代理人交易模擬」

* Agents perform financial research by:

  * Reading stock prices
  * Analyzing real-time financial news
  * Parsing SEC filings & annual reports
  * Making buy/sell decisions
* Simulates trading accounts, **tracks P\&L**, and evolves over time.
* **Bonus detail:** the trading platform is actually written by agents from **Project 5**.
**  系統會模擬帳戶餘額、盈虧狀態等，並使用第 5 專案開發的後台系統作為交易平台。

* **Learning focus:** real-time multi-agent autonomy, retrieval-augmented workflows, financial simulation.
** 學習重點： 實作真正「自主決策型」的多代理人系統，應用在真實世界的商業邏輯（金融科技場景）。
---

### 🧠 Why They Matter

The instructor emphasizes that **Projects 5–8 are the most exciting and commercially valuable**:

* They combine deep **LLM agentic theory** with **hands-on, applied systems**
* They model **real-world B2B/B2C use cases**: software teams, copilots, agent factories, fintech traders
* You’ll build **reusable infrastructure** that mirrors production-level AI agent systems

---

### Setting Up Your Environment
- GitHub repository:
    ```note
    git clone https://www.github.com/christseng89/agents-ai.git
    ```
- Install UV
    ```note
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    uv --version
        uv 0.7.9 (13a86a23b 2025-05-30)
    uv sync
        pyproject.toml
    uv pip install jupyterlab 
    uv run jupyter lab 
    ```
- Create .env
    ```note
    GOOGLE_API_KEY=xxxx
    ANTHROPIC_API_KEY=xxxx
    DEEPSEEK_API_KEY=xxxx
    ```

http://localhost:8888/lab/tree/1_foundations/1_lab1.ipynb

- Using VSC to run Jupyter Lab:
    - Open 1_foundations/1_lab1.ipynb
    - Select the Python kernel (.venv\Python 3.12.10) in the top right corner
    - Run the cells in the notebook
