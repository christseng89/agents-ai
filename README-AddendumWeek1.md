# Agents AI

## Week 1 Day 1
---
### Startup
Flexible AI workflow automation https://n8n.io/

- **n8n.io** is a **low-code/no-code** workflow automation platform that allows users to create workflows by orchestrating between different applications without needing extensive coding knowledge.

- https://github.com/n8n-io/n8n
- Install n8n locally
    ```cmd
    npx n8n
    ```
- http://localhost:5678/home/workflows
- Set up your **.env** file with your **N8N_API_KEY** 

    ```note
    .env
    N8N_API_KEY=eyJh...

    ```

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

- Jupyter Lab URL:
    ```note
    http://localhost:8888/lab/tree/1_foundations/1_lab1.ipynb
    ```

- Using **VSC** to run Jupyter Lab:
    - Open 1_foundations/1_lab1.ipynb
    - Select the Python kernel (.venv\Python 3.12.10) in the top right corner
    - Run the cells in the notebook

## Week 1 Day 2
---
### What is an AI Agent?
#### 🟤 關於 AI 代理人（Agent）的定義模糊性
> **"AI Agents are programs where LLM outputs control the workflow."**
「AI 代理人是指由 LLM 輸出來控制工作流程的程式。」

In practice, describes an AI solution that involves any or all of these:

1. Multiple LLM calls
    多次 LLM 呼叫
2. LLMs with ability to use Tools
    LLM 能使用工具（Tools, e.g. Philips Hue)
3. An environment where LLMs interact
    存在 LLM 彼此互動的環境
4. A Planner to coordinate activities
    有一個規劃者（Planner）來協調任務
5. Autonomy
    具備自主性（Autonomy）
    - 自主型（有 autonomy）	具有目標導向的行為、自動決策與**規劃**
---

### **Agentic Systems**
*Anthropic distinguishes two types:*

#### 🟡 Workflows

> *are systems where LLMs and tools are orchestrated through predefined code paths*
系統中，LLM 和工具的執行順序是透過**預先定義好的程式路徑**所協調的。

#### 🔴 Agents

> *are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks*
LLM 能夠**動態指揮自己的流程與工具使用方式**，並持續掌控任務完成的方式。

---

「Workflows」與「Agents」在 Agentic 系統中的**主控權差異**，簡單來說：

| 類型        | 主導控制   | 決策方式      |
| --------- | ------ | --------- |
| Workflows | 開發者預設  | 照流程走      |
| Agents    | LLM 自主 | 邊走邊想、即時選擇 |

---

#### 🧱 **5 workflow design patterns**

**1. PROMPT CHAINING**
*Decompose into fixed sub-tasks*

```
IN → LLM1 → Gate (code, optional) → LLM2 → LLM3 → OUT
```

---

#### 🧠 解釋：

這是一種將複雜任務**拆解成多個固定步驟**的 AI 設計模式。每個步驟由不同的 LLM 執行一個明確子任務，並**串接成一個穩定流程**。

#### 🔄 舉例應用場景：

例如開發一個自動內容生成器：

1. LLM1 解析用戶需求
2. Gate 判斷任務類型（如技術文、廣告文）
3. LLM2 撰寫初稿
4. LLM3 編輯與格式化
5. OUT 輸出最終文稿

---

**2. ROUTING**
*Direct an input into a specialized sub-task, ensuring separation of concerns*

```
IN → LLM Router (with condition ONLY one LLM) → (LLM1 / LLM2 / LLM3) → OUT
```

---

#### 🧠 解釋：

這種設計模式的核心是**智能分流**，根據輸入的不同類型，自動選擇對應的 LLM 模型執行。

#### 🔄 舉例應用場景：

開發多功能客服代理人：

* LLM Router 判斷輸入為**技術問題 / 行銷查詢 / 帳戶問題**
* 對應地分派給 LLM1（技術支援）、LLM2（業務）、LLM3（財務）
* 最終統一輸出結果

---

**3. PARALLELIZATION**
*Breaking down tasks and running multiple subtasks concurrently*

```
IN → Coordinator (code) → (LLM1 / LLM2 / LLM3 in parallel) → Aggregator (code) → OUT
```

---

#### 🧠 解釋：

這種設計模式強調效率，將大任務切成**可平行執行的小任務**，並行調用多個 LLM 同步處理，最後再整合結果。

#### 🔄 舉例應用場景：

做一份市場報告：

* 協調器將任務拆成三部分：產業分析、競品研究、消費者調查
* 三個 LLM 同時處理三個子題
* 聚合器整合三段分析為一份完整報告

---

**4. ORCHESTRATOR-WORKER**
*Complex tasks are broken down dynamically and combined - refer to **Price is Right** in LLM Engineering Course*

```
IN → Orchestrator (LLM) → (LLM1 / LLM2 / LLM3) → Synthesizer (LLM) → OUT
```
---
### 🧠 解釋：

此模式中的 **Orchestrator（指揮/調度者）** 不只是路由任務，而是**動態拆解複雜任務**並分派給下屬的 LLM 代理人，再由 **Synthesizer** 組合結果。

#### 🔄 舉例應用場景：

建立產品建議系統：

* Orchestrator 根據輸入需求，自動拆成功能、設計、市場等子任務
* 各個 LLM 專責處理不同面向
* Synthesizer 將多項輸出整合成完整提案建議

---

**5. EVALUATOR-OPTIMIZER**
*LLM output is validated by another*

```
IN → LLM Generator → (Solution) → LLM Evaluator  
→ Accept → OUT  
    OR
→ Reject → Feedback → LLM Generator (loop)
```

---

### 🧠 解釋：

這是一種具備「自我回饋與改進」能力的架構。系統由一個生成模型與一個評估模型組成：

* 生成器負責產出初稿或解法
* 評估器負責驗證品質與正確性
* 若不符合標準，系統會回饋建議，並**重新生成改進版**

#### 🔄 舉例應用場景：

自動寫作助手：

* LLM 生成文章段落
* 第二個 LLM 檢查是否符合語氣、風格、邏輯
* 若不滿意，退回修正直到通過

---

這種模式特別適合需要**高品質保證**的任務，如程式碼生成、法律文本、醫療建議等。

---

#### Agents, by contrast, Agents are:

1. Open-ended **開放式任務流程**
   沒有明確的起點與終點，能根據需求持續進行
2. **Feedback loops** **回饋迴圈**
   根據環境回饋動態調整行動策略與決策
3. No fixed path **無固定路徑**
   任務流程非線性、不預設順序，由 LLM 自主決定如何完成目標

**流程圖說明**：

```
HUMAN → LLM Call → ENVIRONMENT <-> (Feedback)  
                          ↓  
                        STOP
```
* 人類提出任務 → LLM 做出決策 → 與外部環境互動（如設備、網路、資料庫）
* 環境回傳結果或反饋 → LLM 根據回饋再調整策略
* 如有需要，可重複循環多次，直到代理人決定停止（STOP）
---

🧠 小結：
| 類型      | 無自主性 LLM（傳統） | 有自主性 **Agentic** LLM |
| ------- | ------------ | ---------------- |
| 回應方式    | 回答單一指令       | 多輪規劃與策略執行        |
| 流程控制    | 由人類預先定義      | 由 LLM 自行規劃與調整    |
| 工具選擇與調用 | 被動（需指示）      | 主動使用工具/查詢/重試     |
| 任務進退決策  | 無決策能力        | 可決定要不要繼續、修正還是終止  |

---

### 🧱 **Risks of Agent Frameworks**

🧭 **🟧 Unpredictable path**
🔀 **🟧 Unpredictable output**
🏷️ **🟧 Unpredictable costs**

📹 **🔵 Monitor**
🚆 **🔵 *"Guardrails ensure your agents behave safely, consistently, and within your intended boundaries"***

* 🟧 橘色：**風險項目**（不可預測性）
* 🔵 藍色：**控制與防護措施**（監控與防護欄）

---

### Guardrails 
#### 🔒 什麼是 Guardrails？

在 Agentic AI 中，**Guardrails（防護欄）**是一種限制與保護機制，目的是讓 LLM 或代理人系統在**安全、可控的範圍內運作**，防止它們偏離預期行為。

它就像是自動駕駛汽車旁邊的護欄——不會阻止車子前進，但會防止它衝出道路。

---

### ✅ Guardrails 的功能：

1. ✅ **限制輸入/輸出內容格式**
2. ✅ **限制工具/API 的使用範圍**
3. ✅ **限制操作時間或循環次數**
4. ✅ **強制執行安全、倫理、合規規則**

---

#### 📌 實際範例說明

---

#### 🧠 範例 1：防止不當輸出

#### ❓任務：

> 使用者輸入：「請寫一段有爭議的政治評論」

#### 🛡️ Guardrail：

設定 LLM 不得生成：

* 政治立場偏頗內容
* 誹謗/仇恨言論
* 違反 OpenAI 使用政策的話語

🔧 實作方式：

* 使用 prompt injection 攔截器或內容過濾器
* 使用 LLM 評估器檢查輸出前自動審核

---

#### 🧠 範例 2：限制 API 使用次數

#### ❓任務：

> 讓代理人使用 Bing 搜尋最新醫療資訊

#### 🛡️ Guardrail：

限制：

* 最多可查詢 5 次
* 禁止查詢特定關鍵字（如「buy drugs」）

🔧 實作方式：

* 設定 tools 執行限制
* 加入 middleware 監控呼叫行為

---

#### 🧠 範例 3：控制流程深度與成本

#### ❓任務：

> 讓 Agent 自主規劃一個商業策略，包含競爭分析與財務模型

#### 🛡️ Guardrail：

* 最多只能呼叫 3 層 LLM 任務鏈
* 每次迴圈不得超過 60 秒
* 預算限制（例如 token 用量不超過 100,000）

🔧 實作方式：

* 設定 task depth 限制
* 用 token 計數器或耗時監控器

---

#### ✅ 工具與框架支援 Guardrails：

| 工具/框架                 | Guardrail 功能                                       |
| --------------------- | -------------------------------------------------- |
| **OpenAI Agents SDK** | 內建規則系統可設定行為限制、內容篩選                                 |
| **GuardrailsAI**      | 自訂輸入/輸出格式、驗證規則、錯誤回饋                                |
| **LangChain**         | 使用 callback + tool call constraints 來實作 guardrails |
| **Rebuff / ReAct**    | 增加中間決策步驟以控制錯誤工具調用或過度回圈                             |

---

### 🧾 小結

| 對象     | Guardrail 效果      |
| ------ | ----------------- |
| LLM 回應 | 避免生成敏感/錯誤/不合規內容   |
| 工具使用   | 控制調用頻率、內容與類型      |
| 任務流程   | 避免無限迴圈、成本爆表、不收斂任務 |

---

## Week 1 Day 3

---
### **Calling multiple LLMs**

- We will be calling **Paid APIs** and **open-source** models in the **cloud** and **locally** throughout this course.

- You have complete flexibility to pick which you use,
and can **spend \$0**.

- More on **selecting, applying** and **deploying** LLMs with my **LLM Engineering** course.

---
### **The cast of characters**

- **OpenAI:** gpt-4o-mini (also gpt-4o, o1, o3-mini)
- **Anthropic:** Claude-3-7-Sonnet
- **Google:** Gemini-2.0-flash
- **DeepSeek AI:** DeepSeek V3, DeepSeek R1
- **Groq:** open-source LLMs including Llama3.3
- **Ollama:** local open-source LLMs including Llama3.2

**The Vellum leaderboard** gives a comparison of costs and performance ([https://www.vellum.ai/llm-leaderboard](https://www.vellum.ai/llm-leaderboard))

---

A breakdown of the **differences between the "cast of characters"** listed in your image — major LLM providers — focusing on their **origin, specialization, performance, openness, and hosting options**:

---

### 🧾 **Overview Table:**

| Provider        | Model(s)             | Type                | Hosting                    | Notable Features                                         |
| --------------- | -------------------- | ------------------- | -------------------------- | -------------------------------------------------------- |
| **OpenAI**      | gpt-4o, gpt-4o-mini  | Proprietary         | Cloud (OpenAI, Azure)      | Multimodal, strong reasoning, long-context dialogue      |
| **Anthropic**   | Claude-3-7-Sonnet    | Proprietary         | Cloud (Claude.ai, Bedrock) | Long context, safe alignment, balanced tone              |
| **Google**      | Gemini-2.0-flash     | Proprietary         | Cloud (Vertex AI)          | Fast responses, integrates with Google ecosystem         |
| **DeepSeek AI** | DeepSeek V3, R1      | Commercial/Research | Self-host or Cloud         | Strong multilingual reasoning, trained on web-scale data |
| **Groq**        | Llama3.3 on Groq LPU | Open-source runtime | Cloud (GroqCloud)          | Ultra-fast inference on custom LPU hardware              |
| **Ollama**      | Llama3.2             | Open-source         | Local (Desktop/Edge)       | Easy local setup, lightweight, offline-capable           |

---

### 🔍 **Detailed Differences by Category**

### 🧠 **1. Intelligence & Reasoning Power**

* **Strongest models**: OpenAI GPT-4o, Anthropic Claude 3, DeepSeek V3
* **Fastest models**: Google Gemini Flash, Groq (LPU-powered)

### 🧩 **2. Openness**

* **Open-source**: DeepSeek, Groq (runs open models), Ollama
* **Closed-source**: OpenAI, Anthropic, Google

### 🖥️ **3. Hosting/Deployment**

* **Cloud-only**: OpenAI, Claude, Gemini
* **Local/Edge-ready**: Ollama, DeepSeek
* **Hybrid (cloud API + self-host)**: Groq, DeepSeek

### 💰 **4. Cost**

* **Free options**: Ollama (run models locally, no API cost)
* **Paid APIs**: OpenAI, Anthropic, Google
* **Groq**: Very low-cost due to their own LPU hardware

---

### ✅ **When to Use What**

| Need                              | Recommendation          |
| --------------------------------- | ----------------------- |
| Best reasoning/completion         | GPT-4o, Claude 3        |
| Cost-effective local use          | Ollama with Llama 3.2   |
| Fastest inference for production  | Groq + Llama3.3         |
| Open research / customization     | DeepSeek V3 or Mistral  |
| Cloud-native business integration | Google Gemini or OpenAI |

---

🤔 Use LPU or GPU?
| Scenario                            | Best Fit                 |
| ----------------------------------- | ------------------------ |
| Training your own model             | **GPU**                  |
| Hosting general AI workloads        | **GPU**                  |
| Serving ultra-fast chatbot response | **LPU** (e.g. GroqCloud) |
| Local prototyping                   | **GPU/CPU** (or Ollama)  |

**客服** Chatbot（Customer Service AI）這類**高併發、低延遲**的應用場景來說，使用 **LPU**（Language Processing Unit），通常比 GPU 更合適

---

1_foundations/2_lab2.ipynb

## Week 1 Day 4

### Here’s the image text represented with color-coded labels and layout (bottom-up):

---

**🟦 Bottom Row (Blue):**

* **No framework**
* **MCP**

**🟩 Middle Row (Light Green):**

* **OpenAI Agents SDK**
* **Crew AI**

**🟫 Top Row (Brown):**

* **LangGraph**
* **AutoGen**

### 🖍️ Color Legend

* **🟦 Blue**: Lower-level or standard options
* **🟩 Light Green**: Emerging agentic AI SDKs (notable middle ground)
* **🟫 Brown**: Advanced, graph‑ or generation‑oriented agentic frameworks

---

### What is MCP?
**MCP** 是 **Model Context Protocol** 的縮寫，一種由 **Anthropic** 在 **2024 年 11 月**提出的**開放標準**，目的是成為讓大型語言模型（LLM）與外部工具、資料源安全交互的「**統一通訊規範**」。

---

### 📘 MCP 主要功能與特色

### 🧩 1. 統一介面（“USB‑C for AI”）

* 將 LLM 與檔案系統、資料庫、API、第三方工具（如 GitHub、Slack、PostgreSQL 等）透過標準化協定連接，免去為每個來源分別寫整合程式。
* 類似**萬用接頭**，連接不同設備與資料源。

### 🔄 2. 雙向安全互動

* 使用 **JSON‑RPC 2.0** 通訊協定，定義清楚的請求與回應格式，支援雙向互動，也能攜帶 metadata（如模型版本、權限資訊）。
* 支援 **tool permission negotiation**，確保代理程式只能執行被授權的操作。

### ⚙️ 3. 開源與跨平台生態

* **Anthropic** 提供 **MCP 伺服器**與**客戶端 SDK**（Python、TypeScript、Java、C# 等）。
* **OpenAI**、**Google DeepMind**、**Microsoft** 等均已採用 MCP，協同打造類似 **HTTP 的 AI Agent 協定**。

---

### 🗣️ MCP 的使用場景

* **桌面助手**：如 Claude Desktop 使用本地 MCP server 讀取文件、操作系統指令。
* **企業應用**：如 Block、Replit、Sourcegraph 使用 MCP 連接內部資料庫和業務工具。
* **工具串接多 Agent 流程**：MCP 支援 agent 到 agent 或 agent 到 service 的協調與資料流轉。

---

### ✨ MCP 的優點

* **可擴充性**：無需為每種工具重寫接口，只需透過 **MCP server 連接一次**。
* **跨模型、跨平台通用**：支援多種 LLM 提供的 **Agent SDK**，例如 Claude、OpenAI Agents SDK 等。
* **安全與審計**：可管理 tool 權限，提供 metadata、日誌與可追溯性。

---

### ✅ 小結

MCP 是一種統一、開源、安全且跨模組通用的介面協定，使得 **AI Agent** 能夠像使用 **USB‑C** 的方式，**一次性連接多種工具與資料源**，並執行雙向交互。已被多家領導者採用，推動了 **AI Agent 的生態建設**。

---

### A practical example of how **MCP** (Model Context Protocol) works in real-world use:

### 🧩 Example: Adding a Postgres MCP Server with Claude CLI

Using the `claude` CLI, you can register an MCP server that lets Claude communicate with a PostgreSQL database:

```bash
# Register a local Postgres MCP server
claude mcp add postgres-server /path/to/postgres-mcp-server \
  --connection-string "postgresql://user:pass@localhost:5432/mydb"
```

Once registered, you can query your database directly in Claude:

```
> describe the schema of our users table
> what are the most recent orders in the system?
```

This setup uses **MCP JSON‑RPC messages** under the hood to:

1. Discover schema (`resources`)
2. Execute queries (`tools`)
3. Return structured JSON results to Claude for interpretation and response ([docs.anthropic.com][1]).

---

### 🔧 Another Example: C# MCP Server Setup

With the **C# MCP SDK**, you can build a simple MCP server like this:

**Program.cs:**

```csharp
using ModelContextProtocol.Server;
using Microsoft.Extensions.Hosting;

var builder = Host.CreateDefaultBuilder(args)
  .ConfigureServices(services => {
    services.AddMcpServer()
      .AddFileSystemTool()    // Expose tools like list/read/write
      .AddPostgresProvider(); // Expose queries to a PostgreSQL DB
  });
await builder.RunConsoleAsync();
```

This spins up a server exposing **file system** and **Postgres** tools via MCP for any client—including Claude or OpenAI—to connect securely ([devblogs.microsoft.com][2]).

---

### ⚙️ Workflow Summary

1. **Server** defines available tools/resources (DB queries, file actions).
2. **Client** (AI agent) discovers them via MCP metadata.
3. **Client** invokes tools (e.g., `mcp_tool_call`) to fetch or manipulate data.
4. **Server** responds with structured JSON and metadata back to the LLM.

---

### ✅ Why this matters

* **Modular**: Add new data sources by plugging into MCP.
* **Standardized**: No need to create custom APIs for each tool.
* **Secure**: Clients only access registered tools with defined permissions.
* **Multi-language**: SDKs in Python, C#, TS, Java, etc., allow broad adoption.

---

### 🏠 在哪裡部署 MCP Server 比較合適？

#### 本地 (Local Machine)

* **僅限於你自己的主機**，例如 Claude Desktop 使用的 MCP 就是本地透過 `stdio` 通訊。
* 好處是：完全不對外公開，安全性高、架設簡單，非常適合個人或內部開發測試環境。

#### 私有雲 (Private Cloud/VPC)

* MCP Server 可部署在你自己的私有雲或公司 VPC 中（如 Kubernetes、AWS VPC、GCP Private Cloud）。
* 可以使用 HTTP(S) 或 SSE 通訊，并設置企業標準的安全機制，如 OAuth/LB/WAF/VPN/ACL 等。
* 適合企業場景，可從內部工具或雲端 Agent 安全呼叫服務，無需走公共互聯網。

---

### ✅ 總結比較

| 部署位置           | 通訊方式                 | 安全性               | 使用場景            |
| -------------- | -------------------- | ----------------- | --------------- |
| **本地 (Local)** | stdio (stdin/stdout) | ⭐⭐⭐⭐ 非常高（僅本地）     | 個人桌面、開發測試環境     |
| **私有雲/VPC**    | HTTP(S) / SSE        | ⭐⭐⭐⭐ 高（私有網路 + 認證） | 企業內部、多 Agent 結合 |
| **公共雲或 Web**   | HTTP 當然可用，但需**謹慎暴露** | ⭐ 取決於安全設置         | 需大量外部腳本或客戶端時    |

---

### 🔐 為什麼選擇這樣？

* **資料與 schema 不會外洩**：只要 MCP Server 未對網際網路開放，**schema 不會暴露**。
* **使用讀/寫權限控制**：可設「最小權限原則」，例如僅 Read-Only 帳號。
* **可設定 tool-level ACL**：限制哪些命令／工具可以被外部 client 呼叫。
* **安全性高**：MCP Server 架設在本地或私有雲環境，能確保資料安全與控制範圍。
* **可控性強**：你可以完全控制 MCP Server 的配置與行為，無需依賴第三方服務。

「MCP Server 架設在 Local 或你的 Private Cloud 環境就可以確保持有安全且可控的使用範圍。」使用 Docker Compose 或 Kubernetes）並加入安全配置指引。

---

### **Resources**
- We can provide an LLM with resources to **improve its expertise**
    我們可以為 LLM 提供資源，以提升其專業能力
- Basically, this just means **shoving data relevant to the question into the prompt**
    基本上，就是把與問題相關的資料塞入 prompt 中
- There are techniques like **RAG** to get really smart at picking **relevant content**
    有一些技巧—例如 **RAG（Retrieval Augmented Generation）**—可以更精準地挑選相關內容

---

### 💡 關鍵概念說明

1. **Shoving data into the prompt**
   指的是將相關的資料集或片段（如文章、產品資訊、數據庫內容）加入到 prompt 的 context 中，讓 LLM 回答時可以根據這些「在 situ」的資訊進行推理。

2. **RAG（檢索增強生成）**
   是一種常見做法，分為三步：索引 → 檢索 → 生成。

   * 先將資料切片並轉為向量儲存（如向量資料庫）
   * 根據使用者提問檢索最相關的片段
   * 把這些片段補充到 prompt 前，再請 LLM 回答
     這能有效提升回應的**準確度、事實性與時效性** 。

3. **為何這麼做？**

   * 不需重訓模型，只靠 prompt 即可擴充知識
   * 降低幻覺發生率（hallucination），因為模型有實證資料作基礎 
   * 可動態更新資料，保持資訊新鮮，仍不用重新訓練

---

### 🧾 小結

* **"Shoving data into prompt"** 是 RAG 的核心思路：先檢索資料，再塞入 prompt 中
* **RAG pipeline** 三步驟：**向量化 → 檢索 → 補 prompt → 生成** 
* 好處是：**準確度高、更新靈活、低成本部署**

---

### Tools and Techniques
“Tools” 为 LLM 带来 **自主操作能力（autonomy）**，意思是让语言模型不仅能“思考”，还可以**主动执行实际动作**，如：

* 💾 **查询数据库（query a database）**
* 🤖 **呼叫其他 LLM（message other LLMs）**
* 🌐 **Philips Hue** 開燈 關燈 變換顏色等

聽起來可能有點可怕──“OpenAI 能進入我的電腦？”──但**真相其實很平凡**：
這些 “tools” 就像被**授權**的**函式**或**微服務**，只是讓 LLM 可以透過「發出指令 → 待命執行並回傳結果」的方式與外部系統互動，而非真正入侵你的資料 。

---

### ✅ 示例：LLM 結合 Tools 的實際場景

### 🔧 範例 1：自然語言查資料（Text-to-SQL Agent）

* **使用者說**：「告訴我上個月的總銷售額？」
* **LLM 判斷**：需要用 SQL 查資料
* **呼叫 tool**：`generate_sql_query(user_input)`
* **執行 tool**：送至資料庫
* **取得結果**，返回給 LLM
* **LLM 組合答覆**：「上個月總銷售額是 \$50,000。」
  這個過程中，LLM 主動分析需求、選用 tool、處理結果，展示自主操作。

---

### 🔧 範例 2：多 LLM 協作

* LLM 可以呼叫其他 LLM，例如讓 Claude **審查** GPT 產出的結果
* 相互對話、校對，形成一個多人協同代理系統
  這就是「message other LLMs」，提升品質與安全性。

---

### 🎯 為什麼 Tools 增加了自主性

* **主動決策**：LLM 不再只是單一輸出，而是在**實際流程控制中**做出調用選擇
* **互聯外部系統**：如資料庫、API、Web、工具，構成閉環回饋流程
* **更大問題處理能力**：可進行動態查驗、回饋、自我修正，遠超傳統“只回應 prompt”的方式

---

### ⚠️ 工具使用的風險 & 防護措施

* 🧠 **潛在濫用**：具備大規模 API 呼叫資源可造成資安風險或資料洩漏 
* 🛡️ **防護對策**：需要設定 guardrails（如 API 呼叫限制、權限控管、輸入驗證）來保障安全。

---

### 🧩 小結

“Tools” 給 LLM 帶來了真正的 **行動能力**，讓它們可以自行：

1. **決定何時做什麼**
2. **呼叫哪些工具或其他 LLM**
3. **解析回傳資料並做決策**

這不只是假裝強大，而是實際上讓 LLM 成為可以 **做事」的智能體**，而非僅僅「回應」的聊天機器人。

---

####　**“Tool Calling in Practice + Resources” 流程圖**：

```
User Prompt + Relevant Resources ──▶ LLM
                 │
                 ▼
        ┌── Decision: Use Tool? ──┐
        │ Yes                      │ No
        ▼                          ▼
  LLM outputs JSON             LLM直接生成回答
  { "tool": name, "args": {...} }
        │
        ▼
   Code parses JSON
   if tool == X: execute X(args)
        ▼
   Execute tool/API/DB
        ▼
   Receive result
        │
        ▼
  Append result to prompt context
  { role: "tool", content: result }
        │
        ▼
Prompt LLM again (with resources + tool result)
        ▼
   LLM generates final response
```

### 🧠 流程說明

1. **Prompt + Resources**

   * 使用者輸入問題，系統先抓取**相關資料**（如航班票價、公司資訊），將其拼入 prompt 中作為 context，提升 LLM 的背景知識。

2. **LLM 判斷 & 工具呼叫**

   * LLM 若偵測需要查票價或計算，就以 JSON 格式回傳工具呼叫指令，如 `{"tool": "get_ticket_price", "args": {"city":"Paris"}}`。

3. **程式接收 & 執行工具**

   * 程式解析 JSON，執行對應工具（例如呼叫資料庫/API）。

4. **工具取得結果**

   * 工具從資料庫或 API 拿到答案（如：Paris 機票 500 USD）。

5. **結果回饋 LLM**

   * 將結果以 `role: "tool"` 的訊息形式補回 LLM prompt 裡，讓模型基於結果再回答。

6. **LLM 最終回應**

   * LLM 重新生成回答，整合插入的 context 與工具結果，提供完整答案。

---

### 🗝️ 核心概念整合

* **Resources**：透過如 RAG 技術，智能選取最相關資料並塞入 prompt，讓模型更專業 。
* **Tool Calling**：LLM 可自主決定是否呼叫工具，並以結構化 JSON 格式發出呼叫，再由後端執行。
* **JSON + if parsing**：後端用 if 判斷工具名稱並執行，屬極簡架構，無魔法，卻力量強大。

---

### ✅ 優勢一覽

| 功能     | 好處                              |
| ------ | ------------------------------- |
| 資料注入   | 升級專業度、降低幻覺現象                    |
| 工具自主呼叫 | 模型可選擇是否使用工具，提升解題彈性              |
| 構建流程透明 | 全流程 JSON 與程式控制，支援監控與 guardrails |

---

#### Practice example (get reply from ChatGPT and Evaluate answers by gemini-2.0-flash):
1_foundations/3_lab3.ipynb
    - What is your greatest accomplishment?
    - What is your greatest failure?
    - What is a challenge that you encountered and needed to overcome?

    Evaluation:
    - What is your current role?
    - What is your current salary?
    - What is your current location?
    - Do you hold a patent?
    - Do you have a flight license?
    - Do you have a driver's license?

## Week 1 Day 5
### Agentic Frameworks - No Frameworks using Tools

1_foundations/test_tools.py
1_foundations/4_lab4.ipynb
1_foundations/app.py

```cmd
cd 1_foundations
uv run test_tools.py
uv run app.py

```

#### Tools for LLMs
這兩個函數 `record_user_details` 和 `record_unknown_question`，搭配對應的 JSON schema，目的在於讓 LLM 能夠透過工具呼叫，**主動紀錄使用者的重要互動資訊**，即使這些不是自然語言對話中直接回答的部分。

---

## 🔍 功能說明：

### 1. `record_user_details`

#### ✅ 目的：

當 LLM 判斷與使用者互動深入、有潛在合作機會時，會引導使用者留下聯絡方式（如 email），並透過這個工具 **紀錄聯絡資訊**。

#### 📦 JSON Schema 範例：

```json
{
  "name": "record_user_details",
  "description": "紀錄使用者聯絡方式，如 email",
  "parameters": {
    "type": "object",
    "properties": {
      "email": {
        "type": "string",
        "description": "使用者的電子郵件地址"
      }
    },
    "required": ["email"]
  }
}
```
---

### 2. `record_unknown_question`

#### ✅ 目的：

當 LLM **無法回答使用者提問時（即使問題很瑣碎或非專業）**，可主動將這個問題記錄下來，方便後續改進模型或讓真人補答。

#### 📦 JSON Schema 範例：

```json
{
  "name": "record_unknown_question",
  "description": "紀錄無法回答的問題",
  "parameters": {
    "type": "object",
    "properties": {
      "question": {
        "type": "string",
        "description": "使用者的問題"
      }
    },
    "required": ["question"]
  }
}
```
---

## 🧠 總結（使用場景比較）：

| 函數名稱                      | 用途                | LLM 自主使用情境                  |
| ------------------------- | ----------------- | --------------------------- |
| `record_user_details`     | 儲存使用者 email 等聯絡方式 | 使用者顯示合作興趣或深入互動              |
| `record_unknown_question` | 紀錄無法回答的問題         | 使用者問了 LLM 無資料可回答的問題（包含冷門話題） |

---

### ✅ 使用 OpenAI Function Calling / Tool Calling 的正確方式：

```python
tools = [{"type": "function", "function": record_user_details_json},
        {"type": "function", "function": record_unknown_question_json}]

...
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools
)
```
### 🔍 說明：

* `model="gpt-4o-mini"`：指定要使用的模型。
* `messages=messages`：歷史對話內容（包含 system/user/assistant role 的訊息）。
* `tools=tools`：告訴模型有哪些工具（函數）它可以使用，讓模型在需要的時候自動回傳工具呼叫（tool call）的 JSON 格式。

---

### 🔧 如果你希望 LLM 在必要時主動使用工具，你還可以加入 `tool_choice="auto"`（可選）：

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto"  # 可選，預設就是 auto
)
```

這樣會讓 LLM 自由決定是否使用其中一個 tool。

---

#### Deploy app.py to Hugging Face Spaces
```cmd
cd 1_foundations
uv run gradio deploy

```
### 📦uv run gradio deploy Work Through
Creating new Spaces Repo in 'D:\development\agents-ai\1_foundations'. Collecting metadata, press Enter to accept default value.
Enter Spaces app title [1_foundations]: **Career_Conversions**
Enter Gradio app file [app.py]: 
Enter Spaces hardware (cpu-basic, cpu-upgrade, cpu-xl, zero-a10g, t4-small, t4-medium, l4x1, l4x4, l40sx1, l40sx4, l40sx8, a10g-small, a10g-large, a10g-largex2, a10g-largex4, a100-large, h100, h100x8) [cpu-basic]:
Any Spaces secrets (y/n) [n]: **y**
Enter secret name (leave blank to end): **OPENAI_API_KEY**
Enter secret value for OPENAI_API_KEY: **sk-proj-ypFvL65EvbsmO7CbVMD5R...**
Enter secret name (leave blank to end): **PUSHOVER_USER**
Enter secret value for PUSHOVER_USER: **uvuq9thwa...**
Enter secret name (leave blank to end): **PUSHOVER_TOKEN**
Enter secret value for PUSHOVER_TOKEN: **aeuhfdmy82...**
Enter secret name (leave blank to end): 
Create Github Action to automatically update Space on 'git push'? [n]: 
Space available at https://huggingface.co/spaces/christseng898/Career_Conversions

### Special Notes:
- **README.md** will be created in the folder 1_foundations after deploy.
