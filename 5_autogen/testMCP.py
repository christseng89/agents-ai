# uvx mcp-server-fetch
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools
from rich import print
from rich.markdown import Markdown

async def main():
    print("Starting AutoGen MCP Server over STDIO...")
    fetch_mcp_server = StdioServerParams(
        command="uvx",
        args=["mcp-server-fetch"],
        errlog=None,                     # ✅ the fix!
        read_timeout_seconds=120,
    )

    print ("Creating MCP Tools...")
    mcp_tools = await mcp_server_tools(fetch_mcp_server)

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    agent = AssistantAgent(
        name="fetcher",
        model_client=model_client,
        tools=mcp_tools,
        reflect_on_tool_use=True
    )

    print ("Running AutoGen Agent...")
    result = await agent.run(
        task="Deeply review edwarddonner.com and summarize what you learn. Reply in Markdown."
    )

    print(Markdown(result.messages[-1].content))

if __name__ == "__main__":
    asyncio.run(main())
