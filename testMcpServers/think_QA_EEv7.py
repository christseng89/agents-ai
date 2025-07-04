#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
triple_mcp_agent_refactor.py
────────────────────────────
把 3 個 MCP (SequentialThinking / Serper / Fetch) 透過 mcpServers 變數管理
"""

import asyncio
import os
from contextlib import AsyncExitStack
from datetime import datetime

from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
from result_utils import print_result

load_dotenv(override=True)

# ── 1. 以「名稱: 設定」形式集中管理 ────────────────────────
mcpServers = {
    "seq_thinking": {  # Sequential-Thinking
        "command": "npx",
        "args": ["--yes", "@modelcontextprotocol/server-sequential-thinking"],
    },
    "serper": {  # Serper Web Search
        "command": "uvx",
        "args": ["serper-mcp-server"],
        "env": {"SERPER_API_KEY": os.getenv("SERPER_API_KEY")},
    },
    "fetch": {  # Fetch URL
        "command": "uvx",
        "args": ["mcp-server-fetch"],
        "env": {"ENABLE_FETCH_IMAGES": "false"},
    },
}

# ── 2. Agent 說明與使用者提問 ───────────────────────────────
instructions = (
    "你是一位 AI 策略顧問。\n"
    "流程：\n"
    "1. 使用 sequentialthinking 工具拆解並記錄思考。\n"
    "2. 如需即時網頁資訊，呼叫 fetch_url (fetch 伺服器) 或 serper_web_search (serper 伺服器)。\n"
    "3. 當 sequentialthinking 回傳 nextThoughtNeeded == false 時，"
    "   將 summary 與必要的外部資訊整合成 Markdown 形式的最終建議。\n"
    "4. 不要在回覆中暴露工具呼叫細節。\n"
)

# ── 2. Agent 說明與使用者提問 ───────────────────────────────
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


# ── 3. 主程式 ───────────────────────────────────────────────
async def main() -> None:
    async with AsyncExitStack() as stack:
        # 3-1 迴圈啟動所有 MCP
        active_servers = {}  # name -> MCPServerStdio
        for name, cfg in mcpServers.items():
            server = await stack.enter_async_context(
                MCPServerStdio(cfg, client_session_timeout_seconds=120)
            )
            active_servers[name] = server
            tools = [t.name for t in await server.list_tools()]
            print(f"{name:<6} tools :", tools)

        # 3-2 建立 Agent（把所有 MCP server 交進去）
        agent = Agent(
            name="TripleMcpAdvisor",
            instructions=instructions,
            mcp_servers=list(active_servers.values()),
            model="gpt-4o-mini",
        )
        print("✔ Agent created:", agent.name)

        # 3-3 執行對話
        with trace("TripleMCPDemo"):
            final_msg = await Runner.run(agent, prompt, max_turns=20)

        # 3-4 輸出與寫檔
        markdown_path = f"qa_plan_{datetime.now():%Y%m%d_%H%M%S}.md"
        content = getattr(final_msg, "content", str(final_msg))
        print_result(final_msg)
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n📄 結果已寫入 {markdown_path}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Interrupted.")
