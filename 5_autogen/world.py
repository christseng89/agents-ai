#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from pathlib import Path

from dotenv import load_dotenv
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost, GrpcWorkerAgentRuntime
from autogen_core import AgentId
from creator import Creator
import messages
from rich.console import Console

load_dotenv(override=True)

console = Console()
# ── 基本設定 ───────────────────────────────
HOW_MANY_AGENTS = 12
OUT_DIR = Path("ideas")
OUT_DIR.mkdir(exist_ok=True)


async def create_and_message(worker: GrpcWorkerAgentRuntime, creator_id: AgentId, i: int):
    try:
        result = await worker.send_message(
            messages.Message(content=f"agent_{i:02d}.py"), creator_id
        )
        (OUT_DIR / f"idea_{i:02d}.md").write_text(result.content)
    except asyncio.CancelledError:
        # 被 Ctrl-C 取消時安靜退出
        raise
    except Exception as e:
        print(f"❌ Worker {i} failed: {e}")


async def main() -> None:
    host = GrpcWorkerAgentRuntimeHost(address="localhost:50052")
    host.start()
    console.print("✅[blue] gRPC Host on localhost:50052")

    worker = GrpcWorkerAgentRuntime(host_address="localhost:50052")
    await worker.start()

    await Creator.register(worker, "Creator", lambda: Creator("Creator"))
    creator_id = AgentId("Creator", "default")

    coroutines = [
        create_and_message(worker, creator_id, i) for i in range(1, HOW_MANY_AGENTS + 1)
    ]

    try:
        # shield 讓 Ctrl-C 不會把 gather 內部 future 留在懸掛狀態
        await asyncio.shield(asyncio.gather(*coroutines))
    except (asyncio.CancelledError, KeyboardInterrupt):
        console.print("\n🛑 [red]Cancelled by user, cleaning up…")
    finally:
        # 無論正常還是中斷，都要優雅收尾
        await worker.stop()
        await host.stop()
        console.print("🧹 [green]gRPC Worker & Host closed.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # asyncio.run 已把 CancelledError 傳遞給 main() 的 finally；這裡不用額外處理
        pass
