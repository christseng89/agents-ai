根據你提供的 Python 程式碼（特別是 `app.py`, `sidekick.py`, `sidekick_tools.py`），以下是這個應用程式的**功能規格書（Functional Specification）**（中文版）：

---

## 📝 功能規格書 – Sidekick 智能助理應用

### 1. 系統簡介

本應用為一個互動式的智能助理系統，結合 OpenAI GPT 模型與工具鏈（如 Playwright、Python、檔案系統、JavaScript 執行等），透過 Gradio UI 提供類 Chatbot 的對話介面。Sidekick 能夠理解使用者需求、選擇工具執行任務，並根據成功條件提供回應或提出問題。

---

### 2. 主要功能模組

#### 2.1 啟動與初始化 (`app_setup`)

* 建立 Sidekick 實例，載入 Playwright 工具、Python 工具、推播通知工具等。
* 初始化語言模型（LLM）並綁定工具鏈。
* 記錄 Sidekick 實例於全域變數 `sidekick_ref` 以便管理。

#### 2.2 使用者訊息處理 (`process_message`)

* 接收來自 Gradio UI 的 `message` 和 `success_criteria`。
* 呼叫 Sidekick 的 `run_superstep()` 方法，驅動整個 LangGraph 任務流程（worker → tool → evaluator）。
* 回傳更新後的對話歷史與 Sidekick 實例。

#### 2.3 重設 Sidekick (`reset`)

* 如果先前有 Sidekick 實例，先釋放資源（browser, playwright 等）。
* 建立全新 Sidekick 實例，進行重新初始化。
* 清空 UI 元件（message, criteria, chatbot）。

#### 2.4 資源釋放機制 (`free_resources`)

* 透過 `atexit` 註冊於應用程式結束時執行。
* 自動關閉 Playwright browser、停止其服務。

---

### 3. Sidekick 任務流程（LangGraph）

#### 3.1 狀態定義 `State`

* `messages`: 對話歷史（支援系統、人類與 AI 訊息）
* `success_criteria`: 成功條件（可選）
* `feedback_on_work`: 評估者回饋
* `success_criteria_met`: 是否滿足成功條件
* `user_input_needed`: 是否需要使用者補充

#### 3.2 Worker

* 根據成功條件與先前回饋構造系統訊息
* 利用 LLM 模型與工具進行推理，並產生回覆
* 若需要工具執行，加入 tool\_calls 標記

#### 3.3 ToolNode

* 使用 LangGraph 預建 ToolNode 統一調用各種工具（瀏覽器、Python、JS、檔案等）

#### 3.4 Evaluator

* 使用第二個 LLM 對 Assistant 回應進行評估
* 回傳是否達成任務與使用者是否需補充資訊
* 可根據之前評估回饋檢查是否重複錯誤

---

### 4. 工具鏈支援（來自 `sidekick_tools.py`）

* ✅ Google 搜尋（Serper）
* ✅ Wikipedia 查詢
* ✅ Python 直譯器
* ✅ Node.js JavaScript 執行
* ✅ Playwright 瀏覽器（非同步）
* ✅ Pushover 推播通知
* ✅ 檔案管理（讀寫、列出、刪除）

---

### 5. 使用者介面（Gradio UI）

* `Chatbot` 顯示與 Sidekick 的對話內容
* `Textbox`:

  * 輸入請求 (`message`)
  * 輸入成功條件 (`success_criteria`)
* `Button`:

  * 「Go!」觸發對話流程
  * 「Reset」清除先前 Sidekick 實例

---

### 6. 錯誤處理與除錯訊息

* 程式中設有 `try/except` 用以處理初始化與資源釋放時錯誤
* 所有步驟均會顯示於 Console，以便除錯
* 特別注意：

  * `RecursionError`：LangGraph 的任務遞迴次數可用 `recursion_limit` 調整
  * `tool.function.name` 限定需符合 `[a-zA-Z0-9_-]` 格式，工具命名應注意

---

如需補充例如：API 認證、錯誤代碼清單、運行環境要求（Python 版本、依賴套件），也可進一步提供。
