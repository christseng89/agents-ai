# Week 5 - Microsoft AutoGen Framework

## **AutoGen** `AG` 

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

### 根據你提供的圖片，以下是 **Microsoft AutoGen 的核心概念（Core Concepts）**，包含對應的圖示與顏色：

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
