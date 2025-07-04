#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autogen_distributed_demo.py
────────────────────────────
• 啟動 GrpcWorkerAgentRuntimeHost
• 註冊 Player1 / Player2 / Judge 3 個 RoutedAgent
• Judge 透過內部對話彙整 Pros / Cons 並做決策
• 支援「單一 Worker」或「多 Worker」佈署
"""
import asyncio
import os
from dataclasses import dataclass
from dotenv import load_dotenv

from autogen_core import AgentId, MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.langchain import LangChainToolAdapter
from autogen_ext.runtimes.grpc import (
    GrpcWorkerAgentRuntime,
    GrpcWorkerAgentRuntimeHost,
)

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
# from IPython.display import display, Markdown
from rich.console import Console
from rich.markdown import Markdown

# ────────────────── 基本設定 ────────────────────
load_dotenv(override=True)
# Initialize Rich console
console = Console()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if not SERPER_API_KEY:
    raise EnvironmentError("請在 .env 或環境變數設定 SERPER_API_KEY")

ALL_IN_ONE_WORKER = False  # True → 三個 agent 同一個 worker

# ────────────────── 資料類型 ────────────────────
@dataclass
class Message:
    content: str

# ────────────────── 共享工具 ────────────────────
serper = GoogleSerperAPIWrapper()
langchain_serper = Tool(
    name="internet_search",
    func=serper.run,
    description="Useful for when you need to search the internet",
)
autogen_serper = LangChainToolAdapter(langchain_serper)

# ────────────────── 指令文字 ────────────────────
instruction1 = (
    "To help with a decision on whether to use AutoGen in a new AI Agent project, "
    "please research and briefly respond with reasons in favor of choosing AutoGen; the pros of AutoGen."
)
instruction2 = (
    "To help with a decision on whether to use AutoGen in a new AI Agent project, "
    "please research and briefly respond with reasons against choosing AutoGen; the cons of AutoGen."
)
judge_prompt = (
    "You must make a decision on whether to use AutoGen for a project. "
    "Your research team has come up with the following reasons for and against. "
    "Based purely on the research from your team, please respond with your decision and brief rationale."
)

# ────────────────── Player / Judge Agent 定義 ───────────────────

class Player1Agent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        print(f"🚀 Initializing {name} Agent...")

        self._delegate = AssistantAgent(
            name,
            model_client=model_client,
            tools=[autogen_serper],
            reflect_on_tool_use=True,
        )

    @message_handler
    async def handle(self, message: Message, ctx: MessageContext) -> Message:
        text_message = TextMessage(content=message.content, source="user")
        resp = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        return Message(content=resp.chat_message.content)


class Player2Agent(Player1Agent):
    pass  # 與 Player1 相同邏輯


class Judge(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        self._delegate = AssistantAgent(name, model_client=model_client)

    @message_handler
    async def handle(self, message: Message, ctx: MessageContext) -> Message:  # <- 改這一行
        inner_1 = AgentId("player1", "default")
        inner_2 = AgentId("player2", "default")

        resp1 = await self.send_message(Message(content=instruction1), inner_1)
        resp2 = await self.send_message(Message(content=instruction2), inner_2)

        combined = (
            f"## Pros of AutoGen:\\n{resp1.content}\\n\\n"
            f"## Cons of AutoGen:\\n{resp2.content}\\n\\n"
        )
        user_msg = TextMessage(
            content=f"{judge_prompt}\\n{combined}\\nRespond with your decision and rationale.",
            source="user",
        )
        print("⚖️  Judge Agent received messages...")
        decision_resp = await self._delegate.on_messages(
            [user_msg], ctx.cancellation_token
        )
        final_text = combined + "## Decision:\\n\\n" + decision_resp.chat_message.content
        return Message(content=final_text)


# ───── 主協程 (修正版) ─────────────────────────────────────
async def main() -> None:
    host = GrpcWorkerAgentRuntimeHost(address="localhost:50052")
    host.start()
    console.print("[green]gRPC Host running on localhost:50052[/]")

    # 依模式建立 worker
    worker1 = worker2 = worker = None
    try:
        if ALL_IN_ONE_WORKER:
            worker = GrpcWorkerAgentRuntime(host_address="localhost:50052")
            await worker.start()

            await Player1Agent.register(worker, "player1", lambda: Player1Agent("player1"))
            await Player2Agent.register(worker, "player2", lambda: Player2Agent("player2"))
            await Judge.register(worker, "judge",   lambda: Judge("judge"))
        else:
            worker1 = GrpcWorkerAgentRuntime(host_address="localhost:50052")
            await worker1.start()
            await Player1Agent.register(worker1, "player1", lambda: Player1Agent("player1"))

            worker2 = GrpcWorkerAgentRuntime(host_address="localhost:50052")
            await worker2.start()
            await Player2Agent.register(worker2, "player2", lambda: Player2Agent("player2"))

            worker = GrpcWorkerAgentRuntime(host_address="localhost:50052")
            await worker.start()
            await Judge.register(worker, "judge", lambda: Judge("judge"))

        # ── 發送初始訊息 ──
        judge_id = AgentId("judge", "default")
        try:
            # shield 讓 Ctrl-C 不會直接取消底層 gRPC；取消時仍可由外層 finally 關閉
            final_resp = await asyncio.shield(
                worker.send_message(Message(content="Go!"), judge_id)
            )
            console.print(Markdown(final_resp.content))
        except asyncio.CancelledError:
            console.print("[yellow]⚠️ 執行被中斷，正在清理…[/]")
            raise

    finally:
        # 優雅關閉所有資源
        if worker is not None:
            await worker.stop()
        if worker1 is not None:
            await worker1.stop()
        if worker2 is not None:
            await worker2.stop()
        await host.stop()
        console.print("[red]🛑 All gRPC servers stopped. Bye![/]")

# ───── 入口點 (修正版) ─────────────────────────────────────
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # asyncio.run 會把 CancelledError 傳遞給 main() 的 finally；
        # 這裡保持安靜即可
        pass