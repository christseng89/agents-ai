## Chinese version

**使用者需求說明（User Requirements Specification）**，用繁體中文撰寫：

---

## ✅ **使用者需求說明：wrapText 函數**

### 🎯 **目標**

開發一個文字包裝與格式控制工具，用於：

* 保留使用者輸入中的換行（`\n`）
* 根據固定寬度自動換行
* 驗證格式是否符合最大行數與最大總長度限制

---

### 📥 **輸入參數**

| 參數         | 類型 | 說明                 |
| ---------- | -- | ------------------ |
| `input`    | 字串 | 使用者輸入的原始文字，可含 `\n` |
| `maxLines` | 整數 | 輸出文字允許的最大行數        |
| `width`    | 整數 | 每行最大可容納的字元數        |

---

### 📐 **功能需求**

#### 1. **處理與分行**

* 將輸入文字中：

  * 移除所有 `\r`（Carriage Return）
  * 去除每行末尾的空白與 tab 字元
* 以 `\n` 為分隔進行切行，**保留空行**

#### 2. **自動換行（Word Wrap）**

* 對每一行文字：

  * 根據空格切分為單字
  * 將單字填入目前行中，當超過 `width` 寬度時進行換行
* 若單字本身長度超過 `width`：

  * 必須**硬切字元**為多行

#### 3. **保留空白行**

* 若原始輸入中有連續的 `\n\n`，則輸出中需對應出現空白行（實體為空字串）

#### 4. **輸出格式**

* 所有行使用 `\n` 相連接
* 最後一行不應額外添加 `\n`

---

### ✅ **驗證條件（Validation）**

#### 1. **最大行數限制**

* 輸出行數不得超過 `maxLines`

#### 2. **總長度限制**

* 計算方式如下：

```text
totalLength = 所有行字元總和 + 2 × (行數 - 1)
```

* 每行之間的斷行視為佔 **2 個字元**
* 不得超過：

```text
maxAllowedLength = maxLines × width + 2 × (maxLines - 1)
```

---

### 🧪 **測試案例驗證準則**

| 類型     | 通過條件                                                 |
| ------ | ---------------------------------------------------- |
| ✅ 成功案例 | 行數 ≤ `maxLines` 且 `totalLength` ≤ `maxAllowedLength` |
| ❌ 失敗案例 | 行數 > `maxLines` 或 `totalLength` > `maxAllowedLength` |

---

### 📘 **範例說明**

#### ✅ 合法輸入：

```text
"12\n\n34"
```

輸出為：

```
12
（空白行）
34
```

* 行數：3 行
* 長度：2 + 0 + 2 + (3 - 1) × 2 = **8** ✅

#### ❌ 不合法輸入：

```text
"12\n\n\n34"
```

* 行數為 4，超出 `maxLines = 3` ❌

```text
"1234567890123456789012345678901"
```

* 字元總數為 31 → 需要 4 行換行 → 超出行數限制或總長度限制 ❌

---

### 📤 **回傳格式**

函數回傳一個物件，格式如下：

```javascript
{
  output: "<處理後文字內容>",  // 最終換行後的文字
  isValid: true | false,        // 是否通過格式驗證
  linesUsed: 整數,              // 實際行數
  totalLength: 整數,            // 總長度
  maxAllowedLength: 整數        // 計算出的最大允許長度
}
```

---

## English version
**User Requirements Specification** based on the behavior and logic implemented in your `wrapText` function and test harness:

---

## ✅ **User Requirements Specification for `wrapText` Function**

### 📌 **Objective**

Implement a text formatting utility that:

* Preserves user-entered line breaks (`\n`)
* Wraps long lines based on a fixed width
* Validates that output meets constraints on total lines and total content length

---

### 📐 **Inputs**

| Parameter  | Type   | Description                             |
| ---------- | ------ | --------------------------------------- |
| `input`    | String | Raw user text input with optional `\n`s |
| `maxLines` | Int    | Maximum allowed lines in final output   |
| `width`    | Int    | Maximum number of characters per line   |

---

### 🧾 **Requirements**

#### 1. **Line Splitting and Cleanup**

* Normalize input by:

  * Removing all carriage returns (`\r`)
  * Trimming trailing spaces/tabs from each line
* Split input by `\n` to preserve user-intended line breaks, including **blank lines**

#### 2. **Word Wrapping Logic**

* For each line:

  * Split into words using whitespace
  * Fit words into lines such that:

    * Each line does not exceed `width` characters
    * Lines wrap at word boundaries
* If a **word is longer than the `width`**, it must be **hard-broken** into multiple lines (substrings)

#### 3. **Blank Line Preservation**

* Each `\n\n` in the input creates a blank line
* Final output must preserve all such blank lines as actual empty lines

#### 4. **Output Construction**

* Resulting lines are joined using `\n`
* No trailing `\n` is added after the last line

---

### ✅ **Validation Rules**

#### 1. **Maximum Line Count**

* The final number of lines **must not exceed `maxLines`**

#### 2. **Maximum Total Length**

* The total output length is calculated as:

```
totalLength = sum_of_characters_in_lines + 2 × (number_of_lines - 1)
```

* Each **line separator** contributes **2 characters**
* The total must not exceed:

```
maxAllowedLength = maxLines × width + 2 × (maxLines - 1)
```

---

### 🧪 **Test Validation Criteria**

| Case Type     | Passes When                                                    |
| ------------- | -------------------------------------------------------------- |
| ✅ **Success** | Line count ≤ `maxLines` and `totalLength` ≤ `maxAllowedLength` |
| ❌ **Failure** | Line count > `maxLines` or `totalLength` > `maxAllowedLength`  |

---

### 🧱 **Examples**

#### ✅ Valid Input

* `"12\n\n34"`

  * Output:

    ```
    12
    (blank)
    34
    ```
  * 3 lines
  * Length = 2 + 0 + 2 + 2×(3-1) = **8** ✅

#### ❌ Invalid Input

* `"12\n\n\n34"`

  * 4 lines → exceeds `maxLines = 3` ❌

* `"1234567890123456789012345678901"`

  * 31 characters → wraps to 4 lines
  * Even if line count OK, `totalLength > maxAllowedLength = 34` ❌

---

### 📤 **Expected Output**

The function should return an object:

```javascript
{
  output: "<wrapped string>",    // newline-separated text
  isValid: true | false,         // based on line/length constraints
  linesUsed: <number>,
  totalLength: <number>,
  maxAllowedLength: <number>
}
```

---
