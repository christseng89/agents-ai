# Week 3 - CrewAI Framework

## Week 3 Day 1

### **CrewAI has several offerings**
*OpenAI and Anthropic have the benefit of not needing a monetization strategy*

- **CrewAI Enterprise**
A multi-agent platform for deploying,
running and monitoring Agentic AI

- **CrewAI UI Studio**
A no-code / lo-code product for
creating multi-agent solutions

- **CrewAI open-source framework** (v)
Orchestrate high performing AI
agents with ease and scale

### **The CrewAI open-source framework comes in two flavors**

- **CrewAI Crews**
    * Autonomous solutions with AI teams
of Agents with different roles

    * Choose **Crews** when: You need autonomous
problem-solving, creative collaboration, or
exploratory tasks


- **CrewAI Flows**
    * Structured automations by dividing
complex tasks into precise workflows

    * Choose **Flows** when: You require deterministic outcomes, auditability, or precise control over execution

### CrewAI Framework **Core concepts**

- **Agent**: an autonomous unit, with an LLM, a role, a goal, a backstory(角色設定), memory, tools
- **Task**: a specific assignment to be carried out, with a description, expected output, agent
- **Crew**: a team of **Agents** and **Tasks**; either:
  - Sequential: run tasks in order they are defined
  - Hierarchical: use a Manager LLM to assign

*Lightweight, but somewhat more opinionated
than OpenAI Agents SDK – more terminology,
marginally more prescriptive*

*..and with an ability to get* **much** *more prescriptive*

### YAML Configuration

**Agents** and **Tasks** can be created by code,
setting the backstory, description, expected output, etc

Or you can define each in a YAML file that's
provided when you create the code:

```yaml
researcher:
  role: >
    Senior Financial Researcher
  goal: >
    Research companies, news and potential
  backstory: >
    You're a seasoned financial researcher with a
    talent for finding the most relevant information.
  llm: openai/gpt-4o-mini
```

```python
agent = Agent(config=self.agents_config['researcher'])
```

## crew\.py

**It all comes together with a Crew definition:**

```python
@CrewBase
class MyCrew():

    @agent
    def my_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['my_agent']
        )

    @task
    def my_task(self) -> Task:
        return Task(
            config=self.tasks_config['my_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )
```

A **sample YAML configuration** that defines both:

* an agent named `my_agent`
* a task named `my_task`

This YAML would correspond directly to what `self.agents_config['my_agent']` and `self.tasks_config['my_task']` are accessing in the Python code.

---

### ✅ `config.yaml` (or split into agents.yaml / tasks.yaml if needed)

```yaml
my_agent:
  role: >
    Market Research Analyst
  goal: >
    Analyze trends and insights from market data to support business decisions.
  backstory: >
    You are a professional market research analyst with 10+ years of experience.
    You are thorough, data-driven, and concise in your reporting.
  llm: openai/gpt-4o-mini

my_task:
  description: >
    Research and summarize recent trends in the EV (electric vehicle) market.
  expected_output: >
    A concise summary of the latest EV industry trends, key players, and potential investment opportunities.
  agent: my_agent
```

---

### LiteLLMs

CrewAI uses the super-simple **LiteLLM** under the hood to interface with almost any LLM; set keys in `.env` file.

```
llm = LLM(model="openai/gpt-4o-mini")
llm = LLM(model="anthropic/claude-3-5-sonnet-latest")
llm = LLM(model="gemini/gemini-2-0-flash")
llm = LLM(model="groq/llama-3-3-70b-versatile")
llm = LLM(model="ollama/llama3.2",
          base_url="http://localhost:11434")

llm = LLM(
    model="openrouter/deepseek/deepseek-r1",
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)
```

*Even **simpler** than **OpenAI Agents SDK.***

### ## CrewAI projects are UV projects

- Install CrewAI with:

```
uv tool install crewai
where crewai
    C:\Users\samfi\.local\bin\crewai.exe
```

### Create a new project with:

```
crewai create crew my_crew

    Creating folder my_crew...
    Cache expired or not found. Fetching provider data from the web...
    Downloading  [####################################]  545153/25572
    Select a provider to set up:
    1. openai
    2. anthropic
    3. gemini
    ...
    13. other
    q. Quit
    Enter the number of your choice or 'q' to quit: 1
    Select a model to use for Openai:
    1. gpt-4
    ...
    5. gpt-4o
    6. gpt-4o-mini
    7. o1-mini
    8. o1-preview
    q. Quit
    Enter the number of your choice or 'q' to quit: 6
    Enter your OPENAI API key (press Enter to skip): 
    API keys and model saved to .env file
    Selected model: gpt-4o-mini
    - Created my_crew\.gitignore
    ...
    - Created my_crew\src\my_crew\config\tasks.yaml
    Crew my_crew created successfully!
```

This creates an entire directory structure:

```
my_crew
└── src
    └── my_crew
        ├── config
        │   ├── agents.yaml
        │   └── tasks.yaml
        ├── crew.py
        └── main.py
```

### Run with

```
crewai run
    Running the Crew
    Using CPython 3.12.10
    Creating virtual environment at: .venv
        Built chroma-hnswlib==0.7.6
    ░░░░░░░░░░░░░░░░░░░░ [0/198] Installing wheels.
    ...
    ╭──────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────╮
    │  Crew Execution Completed                                                                                        │
    │  Name: crew                                                                                                      │
    │  ID: ce1e346c-a62a-42ff-a370-d7dd72181300                                                                        │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

### 'motion': 'There needs to be strict laws to regulate LLMs'

```cmd
cd 3_crew\debate
crewai run
```
...
🚀 Crew: crew
├── 📋 Task: 0ab9b095-a429-469b-8411-ce74dc03d32a
│      Assigned to: A compelling debater
│      Status: ✅ Completed
│   └── 🤖 Agent: A compelling debater
│           Status: ✅ Completed
├── 📋 Task: dc040faa-e78a-4aab-af55-b5be0b47db95
│      Assigned to: A compelling debater
│      Status: ✅ Completed
│   └── 🤖 Agent: A compelling debater
│           Status: ✅ Completed
└── 📋 Task: bd2e5c44-02a1-4a49-9792-bd458442e383
       Assigned to: Decide the winner of the debate based on the arguments presented
       Status: ✅ Completed
    └── 🤖 Agent: Decide the winner of the debate based on the arguments presented
            Status: ✅ Completed
╭──────────────────────────────────────────────────────── Task Completion ──────╮
│  Task Completed                                                               │
│  Name: bd2e5c44-02a1-4a49-9792-bd458442e383                                   │
│  Agent: Decide the winner of the debate based on the arguments presented      │
╰───────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────── Crew Completion ──────╮
│  Crew Execution Completed                                                     │
│  Name: crew                                                                   │
│  ID: 3db38bf0-d97c-4ebb-8be4-04037bfe6f2c                                     │
╰───────────────────────────────────────────────────────────────────────────────╯

## Week 3 Day 2 - Financial Researcher Crew

### ✅ Recap
- 🤖 **Agent**：an autonomous unit, with an LLM, a role, a goal, a backstory, memory, tools
- 🧡 **Task**：a specific assignment to be carried out, with a description, expected output, agent
- 🔵 **Crew**：a team of **Agents** and **Tasks**; either:
  • **Sequential**: run tasks in order they are defined
  • **Hierarchical**: use a Manager LLM to assign

---

### 🪜 Five Steps

**1️⃣** Create the project with:
 `crewai create crew my_project`

**2️⃣** Fill in the config YAML files to define the
 **Agents** and **Tasks**

**3️⃣** Complete the `crew.py` module to create the
 **Agents**, **Tasks**, and **Crew**, referencing the config

**4️⃣** Update `main.py` to setup any inputs and run

**5️⃣** Run with:
 `crewai run`

---

### 🔍 Going deeper

🛠 **Tools**
 Equipping agents with capabilities

ℹ️ **Context**
 Information passed from 1 task to another

---

### The World's Fastest & Cheapest Google Search API
https://serper.dev/

- Sign up for a free account samfire5201@gmail.com
- Get your API key

### Financial Researcher Crew 'company': 'Apple'

```
cd 3_crew\financial_researcher
crewai run
```

## Week 3 Day 3 - Stock Picker Crew
### 📂 Going deeper again..

- 🧱  Structured outputs
- 🧭  Custom Tool
- ▦  Hierarchical process

```cmd
cd 3_crew\stock_picker
crewai run
```

### 🧱 Structured Outputs

crew.py
```python
...
class TrendingCompany(BaseModel):
    """ A company that is in the news and attracting attention """
    name: str = Field(description="Company name")
    ticker: str = Field(description="Stock ticker symbol")
    reason: str = Field(description="Reason this company is trending in the news")

class TrendingCompanyList(BaseModel):
    """ List of multiple trending companies that are in the news """
    companies: List[TrendingCompany] = Field(description="List of companies trending in the news")

class TrendingCompanyResearch(BaseModel):
    """ Detailed research on a company """
    name: str = Field(description="Company name")
    market_position: str = Field(description="Current market position and competitive analysis")
    future_outlook: str = Field(description="Future outlook and growth prospects")
    investment_potential: str = Field(description="Investment potential and suitability for investment")

class TrendingCompanyResearchList(BaseModel):
    """ A list of detailed research on all the companies """
    research_list: List[TrendingCompanyResearch] = Field(description="Comprehensive research on all trending companies")

...

```
### 🧭 Custom Tool

```python crew.py
from .tools.push_tool import PushNotificationTool
...
    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_picker'], 
            tools=[PushNotificationTool()], 
            memory=True
            )
...            
```
### ▦  Hierarchical process

```python crew.py
    @crew
    def crew(self) -> Crew:
        """Creates the StockPicker crew"""

        # ❌ Manager 不應有 tools, CrewAI Manager agent 的角色定位是「協調者」，而不是執行者
        manager = Agent(
            config=self.agents_config['manager'],
            allow_delegation=True
        )
            
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.hierarchical, # Hierarchical process for structured task management
            verbose=True,
            manager_agent=manager,
            ...)

```

## Week 3 Day 4 - **CrewAI Memory**
### **CrewAI Memory – more prescriptive**

🟡 **Short-Term Memory**
Temporarily stores recent interactions and outcomes using RAG, enabling agents to access relevant information during the current executions.

🟡 **Long-Term Memory**
Preserves valuable insights and learnings, building knowledge over time.

🟡 **Entity Memory**
Information about people, places and concepts encountered during tasks, facilitating deeper understanding and relationship mapping. Uses RAG for storing entity information.

🟠 **Contextual Memory**
Maintains the context of interactions by combining all the above.

🔵 **User Memory**
Stores user-specific information and preferences, enhancing personalization and user experience (this is up to us to manage and include in prompts).

🧠 Summary Table:
| Memory Type       | Uses Vector DB (RAG) | Notes                                                |
| ----------------- | -------------------- | ---------------------------------------------------- |
| Short-Term Memory | ✅ Yes                | Stores recent task context in embedding format       |
| Entity Memory     | ✅ Yes                | Embeds entity knowledge for retrieval                |
| Long-Term Memory  | ❌/🔄 Optional        | May store structured insights, optionally vectorized |
| Contextual Memory | ❌ Indirectly         | Aggregates others; not a store itself                |
| User Memory       | ❌ No                 | Structured user-specific data; not vector-based      |

---

```code crew.py
...
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
...
    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_company_finder'],
            tools=[SerperDevTool()], 
            memory=True # Enable memory for the trending company finder agent
        )

    ...
    
    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_picker'], 
            tools=[PushNotificationTool()], 
            memory=True # Enable memory for the stock picker agent
        )
    ...
    @crew
    def crew(self) -> Crew:
        """Creates the StockPicker crew"""

        # ❌ Manager 不應有 tools, CrewAI Manager agent 的角色定位是「協調者」，而不是執行者
        manager = Agent(
            config=self.agents_config['manager'],
            allow_delegation=True
        )

        # Long-term memory for persistent storage across sessions
        long_term_memory = LongTermMemory(
            storage=LTMSQLiteStorage(
                db_path="./memory/long_term_memory_storage.db"
            )
        )            

        # Short-term memory for current context using RAG
        short_term_memory = ShortTermMemory(
            storage = RAGStorage(
                embedder_config={
                    "provider": "openai",
                    "config": {
                        "model": 'text-embedding-3-small'
                    }
                },
                type="short_term",
                path="./memory/"
            )
        )
        
        # Entity memory for tracking key information about entities
        entity_memory = EntityMemory(
            storage=RAGStorage(
                embedder_config={
                    "provider": "openai",
                    "config": {
                        "model": 'text-embedding-3-small'
                    }
                },
                type="short_term",
                path="./memory/"
            )
        )
        
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.hierarchical, # Hierarchical process for structured task management
            verbose=True,
            manager_agent=manager,
            memory=True,
            long_term_memory = long_term_memory,
            short_term_memory = short_term_memory,
            entity_memory = entity_memory,
        )

```
✅ Memory Summary Table

| On disk (what you saw)               | Comes from …                    | Memory type                           | Backend             |
| ------------------------------------ | ------------------------------- | ------------------------------------- | ------------------- |
| `memory/long_term_memory_storage.db` | `LTMSQLiteStorage`              | **Long-Term Memory**                  | SQLite              |
| `memory/chroma.sqlite3`              | `RAGStorage` (Chroma) | **Short-Term Memory** (vector based)            | Chroma vector store |
| `memory/<uuid>/{data_level0.bin, …}` | `RAGStorage` (FAISS)            | **Entity Memory** (also vector based) | FAISS index         |

`memory/chroma.sqlite3`: 📦 Chroma 向量資料庫的 SQLite 儲存格式。

### Short-Term Memory vs Entity Memory
While both **`ShortTermMemory` and `EntityMemory` technically use short-term vector storage**, they serve **very different purposes** in an AI agent's memory system. Here's the key distinction:

---

### 🧠 1. `ShortTermMemory`（短期記憶）

| 項目              | 說明                          |
| --------------- | --------------------------- |
| **目標**          | 保持「最近上下文」的記憶，用來幫助當前對話或任務的理解 |
| **儲存內容**        | 最近的任務輸出、對話紀錄、推理過程等通用資訊      |
| **使用場景**        | 對話銜接、多輪推理、分析前一步驟結果時         |
| **是否具備語意檢索功能？** | ✅ 是（例如用 embedding 找回最近相關句子） |

🔁 類似於人類的「剛剛說過什麼」。

---

### 🧬 2. `EntityMemory`（實體記憶）

| 項目              | 說明                                 |
| --------------- | ---------------------------------- |
| **目標**          | 長期追蹤「具名實體」的資訊，例如某公司、某人、某地點         |
| **儲存內容**        | 關於特定實體的屬性、關係、背景，例如 `OpenAI 是由誰創立？` |
| **使用場景**        | 多輪任務中持續提及相同對象，並需要一致性回答             |
| **是否具備語意檢索功能？** | ✅ 是（但聚焦於特定實體）                      |

🔁 類似於人類腦中對「熟人」或「公司」的記憶片段。

---

### 📊 對比總表

| 特性     | `ShortTermMemory` | `EntityMemory`          |
| ------ | ----------------- | ----------------------- |
| 用途     | 幫助 AI 記住最近事件      | 幫助 AI 記住具名實體的背景         |
| 例子     | 上一步分析結果、使用者問句     | 公司名稱、人物、地名              |
| 記憶持續性  | 一次任務內（通常會清除）      | 多次任務可共享（如設定 Entity key） |
| 向量存儲方式 | 通用段落＋embedding    | 實體關聯資訊＋embedding        |
| 常用任務   | RAG context, 推理銜接 | 知識抽取、背景延續               |

---

### ✅ 結論

* `ShortTermMemory`: 記「最近事件的語境」
* `EntityMemory`: 記「特定主體的背景與關聯」

可以**同時啟用兩者**來讓 Agent 表現更像人類：又能記住剛剛說什麼，也能牢記你是誰、你說過什麼事。

---

### **Giving coding skills to an Agent**

It’s **<span style="color:red">hard</span>** and it’s **<span style="color:orange">complex</span>**, but you can have an Agent
in Crew that has the ability to write code, execute it
in a **Docker container**, and investigate the results.

**<span style="color:gold">Except it’s not.</span>**

```python
Agent(
    allow_code_execution=True,
    code_execution_mode="safe"
)
```

These are often described as **"Coder Agents** with coding skills.

---

```
cd 3_crew\coder
crewai run
```
