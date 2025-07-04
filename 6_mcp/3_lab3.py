from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
import os
# from IPython.display import Markdown, display
from datetime import datetime
from polygon import RESTClient

import asyncio
from rich.console import Console
from rich.markdown import Markdown
from market import get_share_price

load_dotenv(override=True)
# Initialize Rich console
console = Console()

def print_tools(tools):
    """Helper function to print tool names and descriptions."""
    for tool in tools:
        print(f"🛠️  Tool name: {tool.name} \n   Description: {tool.description}")

def print_result(result):
    """Helper function to print the final output of the agent."""
    # display(Markdown(result.final_output))
    console.print(Markdown(result.final_output))
    print("\n")

async def main():
    # The first type of MCP Server runs locally, everything local
    print("\n🚀  Starting Memory DB MCP Server...")
    params = {
        "command": "npx",
        "args": ["-y", "mcp-memory-libsql"],
        "env": {"LIBSQL_URL": "file:./memory/ed.db"}
        }
    
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        mcp_tools = await server.list_tools()

    print_tools(mcp_tools)

    print("\n🚀  Starting Memory DB MCP Server with Agent...")
    instructions = "You use your entity tools as a persistent memory to store and recall information about your conversations."
    request = "My name's Ed. I'm an LLM engineer. I'm teaching a course about AI Agents, including the incredible MCP protocol. \
    MCP is a protocol for connecting agents with tools, resources and prompt templates, and makes it easy to integrate AI agents with capabilities."
    model = "gpt-4.1-mini"

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, request)
        # display(Markdown(result.final_output))
        print_result(result)

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, "My name's Ed. What do you know about me?")
        # display(Markdown(result.final_output))
        print_result(result)

    # The 2nd type of MCP server - runs locally, calls a web service
    print("\n🚀  Starting Brave Search MCP Server...")
    # env = {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
    params = {
        "command": "npx", 
        "args": ["-y", "@modelcontextprotocol/server-brave-search"], 
        "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
        }

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        mcp_tools = await server.list_tools()

    print_tools(mcp_tools)

    print("\n🚀  Starting Brave Search MCP Server with Agent...")
    instructions = "You are able to search the web for information and briefly summarize the takeaways."
    request = f"Please research the latest news on Amazon stock price and briefly summarize its outlook. \
    For context, the current date is {datetime.now().strftime('%Y-%m-%d')}"
    model = "gpt-4o-mini"

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, request)
        # display(Markdown(result.final_output))
        print_result(result)

    # And now the third type: running remotely

    polygon_api_key = os.getenv("POLYGON_API_KEY")
    print (polygon_api_key[:8])
    if not polygon_api_key:
        print("POLYGON_API_KEY is not set")

    client = RESTClient(polygon_api_key)
    client.get_previous_close_agg("AAPL")[0]

    get_share_price("AAPL")

    # no rate limiting concerns!

    for i in range(1000):
        get_share_price("AAPL")
    get_share_price("AAPL")

    print("\n🚀  Starting MCP Server with Market API...")
    params = {
        "command": "uv", 
        "args": ["run", "market_server.py"]
        }
    
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        mcp_tools = await server.list_tools()

    print_tools(mcp_tools)

    instructions = "You answer questions about the stock market."
    request = "What's the share price of Apple?"
    model = "gpt-4.1-mini"

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, request)
        # display(Markdown(result.final_output))
        print_result(result)

    print("\n🚀  Starting MCP Server with Polygon API...")
    params = {
        "command": "uvx",
        "args": ["--from", "git+https://github.com/polygon-io/mcp_polygon@v0.1.0", "mcp_polygon"],
        "env": {"POLYGON_API_KEY": polygon_api_key}
        }
    
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        mcp_tools = await server.list_tools()
   
    print_tools(mcp_tools)

    instructions = "You answer questions about the stock market."
    request = "What's the share price of Apple? Use your get_snapshot_ticker tool to get the latest price."
    model = "gpt-4.1-mini"

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, request)
        # display(Markdown(result.final_output))
        print_result(result)

    polygon_plan = os.getenv("POLYGON_PLAN")
    is_paid_polygon = polygon_plan == "paid"
    is_realtime_polygon = polygon_plan == "realtime"

    if is_paid_polygon:
        print("You've chosen to subscribe to the paid Polygon plan, so the code will look at prices on a 15 min delay")
    elif is_realtime_polygon:
        print("Wowzer - you've chosen to subscribe to the realtime Polygon plan, so the code will look at realtime prices")
    else:
        print("According to your .env file, you've chosen to subscribe to the free Polygon plan, so the code will look at EOD prices")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Shutdown requested — exiting…")  
