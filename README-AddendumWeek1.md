# Agents AI

## Week 1 Day 1
---
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
IN → LLM Router → (LLM1 / LLM2 / LLM3) → OUT
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
*Complex tasks are broken down dynamically and combined*

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

#### Guardrails
### 🔒 什麼是 Guardrails？

在 Agentic AI 中，**Guardrails（防護欄）**是一種限制與保護機制，目的是讓 LLM 或代理人系統在**安全、可控的範圍內運作**，防止它們偏離預期行為。

它就像是自動駕駛汽車旁邊的護欄——不會阻止車子前進，但會防止它衝出道路。

---

## ✅ Guardrails 的功能：

1. ✅ **限制輸入/輸出內容格式**
2. ✅ **限制工具/API 的使用範圍**
3. ✅ **限制操作時間或循環次數**
4. ✅ **強制執行安全、倫理、合規規則**

---

## 📌 實際範例說明

---

### 🧠 範例 1：防止不當輸出

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

### 🧠 範例 2：限制 API 使用次數

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

### 🧠 範例 3：控制流程深度與成本

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

### ✅ 工具與框架支援 Guardrails：

| 工具/框架                 | Guardrail 功能                                       |
| --------------------- | -------------------------------------------------- |
| **OpenAI Agents SDK** | 內建規則系統可設定行為限制、內容篩選                                 |
| **GuardrailsAI**      | 自訂輸入/輸出格式、驗證規則、錯誤回饋                                |
| **LangChain**         | 使用 callback + tool call constraints 來實作 guardrails |
| **Rebuff / ReAct**    | 增加中間決策步驟以控制錯誤工具調用或過度回圈                             |

---

## 🧾 小結

| 對象     | Guardrail 效果      |
| ------ | ----------------- |
| LLM 回應 | 避免生成敏感/錯誤/不合規內容   |
| 工具使用   | 控制調用頻率、內容與類型      |
| 任務流程   | 避免無限迴圈、成本爆表、不收斂任務 |

---
