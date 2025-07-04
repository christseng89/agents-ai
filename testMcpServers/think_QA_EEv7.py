#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sequential_thinking_with_serper_and_fetch.py
一次啟動 3 個 MCP 伺服器（SequentialThinking / Serper / Fetch），
讓 Agent 自行使用工具並把最終結果寫入 markdown。
"""
import asyncio
import os
from contextlib import AsyncExitStack
from datetime import datetime

from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
from result_utils import print_result  # 你原本的輔助函式

load_dotenv(override=True)            # 讀取 OPENAI_API_KEY / SERPER_API_KEY

# ── MCP 伺服器設定 ──────────────────────────────────────────
SEQ_SERVER_CFG = {
    "command": "npx",
    "args": ["--yes", "@modelcontextprotocol/server-sequential-thinking"],
}

SERPER_SERVER_CFG = {
    "command": "uvx",
    "args": ["serper-mcp-server"],
    "env": {"SERPER_API_KEY": os.getenv("SERPER_API_KEY")},
}

FETCH_SERVER_CFG = {
    "command": "uvx",
    "args": ["mcp-server-fetch"],
    # 如需下載圖片請移除下行
    "env": {"ENABLE_FETCH_IMAGES": "false"},
}

# ── Agent 說明與 Prompt ───────────────────────────────────
instructions = (
    "你是一位 AI 策略顧問。\n"
    "流程：\n"
    "1. 使用 sequentialthinking 工具拆解並記錄思考。\n"
    "2. 如需即時網頁資訊，呼叫 fetch_url (fetch 伺服器) 或 serper_web_search (serper 伺服器)。\n"
    "3. 當 sequentialthinking 回傳 nextThoughtNeeded == false 時，"
    "   將 summary 與必要的外部資訊整合成 Markdown 形式的最終建議。\n"
    "4. 不要在回覆中暴露工具呼叫細節。\n"
)

prompt = (
    "我們想將舊版 Java EE 應用導入新版 SaaS 的 QA 作業，"
    "並利用 Terraform、BDD、UiPath 等工具，將測試流程全面自動化。\n"
    "目標涵蓋：\n"
    "1. 舊版環境自動部署並匯入測試案例，產生結果①；\n"
    "2. 資料遷移至新版環境，以相同測試案例產生結果②；\n"
    "3. 自動比對結果①與結果②（含差異報告與可追溯日誌）。\n\n"
    "請列出為達成自動化所需的完整準備清單"
    "（基礎設施、工具選型、測試資料、比對策略、CI/CD 整合、回滾方案等），"
    "並說明每一項的關鍵考量與最佳實踐，輸出格式請用 Markdown。"
)

# ── 主程式 ─────────────────────────────────────────────────
async def main() -> None:
    async with AsyncExitStack() as stack:
        sequential_mcp = await stack.enter_async_context(
            MCPServerStdio(SEQ_SERVER_CFG, client_session_timeout_seconds=120)
        )
        serper_mcp = await stack.enter_async_context(
            MCPServerStdio(SERPER_SERVER_CFG, client_session_timeout_seconds=60)
        )
        fetch_mcp = await stack.enter_async_context(
            MCPServerStdio(FETCH_SERVER_CFG, client_session_timeout_seconds=60)
        )

        # 列出各伺服器工具
        print("Sequential tools :", [t.name for t in await sequential_mcp.list_tools()])
        print("Serper     tools :", [t.name for t in await serper_mcp.list_tools()])
        print("Fetch      tools :", [t.name for t in await fetch_mcp.list_tools()])

        # 建立 Agent
        thinker = Agent(
            name="SequentialThinker",
            instructions=instructions,
            mcp_servers=[sequential_mcp, serper_mcp, fetch_mcp],
            model="gpt-4o-mini",
        )
        print("✔ Agent created:", thinker.name)

        # 執行對話
        with trace("SeqDemo"):
            final_msg = await Runner.run(thinker, prompt, max_turns=20)

        # 螢幕輸出
        print_result(final_msg)

        # 將內容寫入 Markdown 檔
        markdown_path = f"qa_automation_plan_{datetime.now():%Y%m%d_%H%M%S}.md"
        content = getattr(final_msg, "content", str(final_msg))
        with open(markdown_path, "w", encoding="utf-8") as md_file:
            md_file.write(content)
        print(f"\n📄 已將結果寫入 {markdown_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Demo interrupted by user.")
