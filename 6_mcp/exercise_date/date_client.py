# date_client.py

import mcp
from mcp.client.stdio import stdio_client   # ✅ ADD THIS IMPORT!
from mcp import StdioServerParameters

params = StdioServerParameters(
    command="uv",
    args=["run", "date_server.py"],
    env=None
)

async def call_get_today_date():
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.call_tool("get_today_date", {})

            # Debug print
            # print("DEBUG result:", result)

            if result.content and hasattr(result.content[0], "text"):
                return result.content[0].text
            else:
                return str(result)
