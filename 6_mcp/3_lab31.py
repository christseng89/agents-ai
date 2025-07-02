# full_example.py

import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
# from IPython.display import Markdown, display
from rich.console import Console
from rich.markdown import Markdown
from market import get_share_price, get_share_price_polygon_eod
from market_server import get_available_symbols

load_dotenv(override=True)
# Initialize Rich console
console = Console()

def print_tools(tools):
    """Helper function to print tool names and descriptions."""
    for tool in tools:
        print(f"🛠️  Tool name: {tool.name} \n   Description: {tool.description}")

def print_result(result):
    """Helper function to print the final output of the agent."""
    print("\nResults:")
    console.print(Markdown(result.final_output))

async def main():
    # 示例：內部 memory DB MCP Server
    print("\n🚀  Starting Memory DB MCP Server...")
    params = {
        "command": "npx", 
        "args": ["-y", "mcp-memory-libsql"], 
        "env": {"LIBSQL_URL": "file:./memory/ed.db"}
        }
    
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        tools1 = await server.list_tools()
        print("Memory DB tools:\n")
        print_tools(tools1)

        # Agent 範例：儲存記憶
        instructions = "You use your entity tools as persistent memory."
        agent = Agent(
            name="agent", 
            instructions=instructions, 
            model="gpt-4.1-mini", 
            mcp_servers=[server]
            )
        with trace("conv11"):
            result11 = await Runner.run(agent, "My name's Ed. I'm an LLM engineer.")

        print_result(result11)

        with trace("conv12"):
            result12 = await Runner.run(agent, "My name's Ed. What do you know about me?")

        print_result(result12)

    # 示例：Brave Search MCP
    print("\n🚀  Starting Brave Search MCP Server...")
    params2 = {
        "command": "npx", 
        "args": ["-y", "@modelcontextprotocol/server-brave-search"], 
        "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
        }
    async with MCPServerStdio(params=params2, client_session_timeout_seconds=30) as server2:
        tools2 = await server2.list_tools()
        print("Brave Search tools\n")
        print_tools(tools2)

        instructions2 = "You are able to search the web and summarize."
        agent2 = Agent(
            name="agent2", 
            instructions=instructions2, 
            model="gpt-4o-mini", 
            mcp_servers=[server2]
            )
        with trace("conv2"):
            user_request = f"Research latest Amazon stock price. Current date {datetime.now().strftime('%Y-%m-%d')}"
            result2 = await Runner.run(agent2, user_request)

        print_result(result2)

    # 示例：Market MCP Server
    print("\n🚀  Starting Market MCP Server...")
    params3 = {
        "command": "uv", 
        "args": ["run", "market_server.py"], 
        "env": None
        }
    async with MCPServerStdio(params=params3, client_session_timeout_seconds=30) as server3:
        tools3 = await server3.list_tools()
        print("Market tools:")
        print_tools(tools3)

        instructions3 = "Answer questions about the stock market."
        agent3 = Agent(
            name="agent3", 
            instructions=instructions3, 
            model="gpt-4.1-mini", 
            mcp_servers=[server3]
            )
        with trace("conv31"):
            result31 = await Runner.run(agent3, "What's the share price of Apple?")
        print_result(result31)

        with trace("conv32"):
            result32 = await Runner.run(agent3, "What's the share price of Amazon?")
        print_result(result32)

        with trace("conv33"):
            result33 = await Runner.run(agent3, "What's the share price of Tesla?")
        print_result(result33)

    print("\nDirectly using market.py via Polygon API ...")
    print(f"Get Price: {get_share_price('AAPL')}")
    print(f"EOD Price: {get_share_price_polygon_eod('AAPL')}")

    print("\nDirectly using market_server.py ...")
    print(await get_available_symbols())

    
if __name__ == "__main__":
    asyncio.run(main())
