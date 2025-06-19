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
