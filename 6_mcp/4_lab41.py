#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import asyncio
import json
from dotenv import load_dotenv
from agents import Agent, Runner, trace, Tool
from agents.mcp import MCPServerStdio
from rich.console import Console
from rich.markdown import Markdown
from datetime import datetime
from accounts_client import read_accounts_resource, read_strategy_resource
from accounts import Account
from traders import Trader
from reset import reset_traders
from mcp_params import researcher_mcp_server_params, trader_mcp_server_params

from result_utils import print_result

# Load .env
load_dotenv(override=True)

# Rich console for pretty output
console = Console()

# Create the researcher agent
async def get_researcher(mcp_servers) -> Agent:
    instructions = f"""You are a financial researcher. You are able to search the web for interesting financial news,
look for possible trading opportunities, and help with research.
Based on the request, you carry out necessary research and respond with your findings.
Take time to make multiple searches to get a comprehensive overview, and then summarize your findings.
If there isn't a specific request, then just respond with investment opportunities based on searching latest news.
The current datetime is {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    researcher = Agent(
        name="Researcher",
        instructions=instructions,
        model="gpt-4.1-mini",
        mcp_servers=mcp_servers,
    )
    return researcher

# Wrap researcher as a tool
async def get_researcher_tool(mcp_servers) -> Tool:
    researcher = await get_researcher(mcp_servers)
    return researcher.as_tool(
            tool_name="Researcher",
            tool_description="This tool researches online for news and opportunities, \
                either based on your specific request to look into a certain stock, \
                or generally for notable financial news and opportunities. \
                Describe what kind of research you're looking for."
        )


# Environment variables
polygon_api_key = os.getenv("POLYGON_API_KEY")
polygon_plan = os.getenv("POLYGON_PLAN")

is_paid_polygon = polygon_plan == "paid"
is_realtime_polygon = polygon_plan == "realtime"

print("is_paid_polygon:", is_paid_polygon)
print("is_realtime_polygon:", is_realtime_polygon)

# Market MCP params
if is_paid_polygon or is_realtime_polygon:
    market_mcp = {
        "command": "uvx",
        "args": [
            "--from",
            "git+https://github.com/polygon-io/mcp_polygon@master",
            "mcp_polygon"
        ],
        "env": {
            "POLYGON_API_KEY": polygon_api_key
        }
    }
else:
    market_mcp = {
        "command": "uv",
        "args": ["run", "market_server.py"]
    }

# Researcher MCP params
brave_env = {
    "BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")
}


mcp_server_params = [
    {"command": "uvx", "args": ["mcp-server-fetch"]},
    {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-brave-search"], "env": brave_env}
]

# Main async function
async def main():
    # Now create the MCPServerStdio for 
    
    researcher_mcp_servers = [
        MCPServerStdio(params, client_session_timeout_seconds=120) 
        for params in mcp_server_params
        ]
    trader_mcp_servers = [
        MCPServerStdio(params, client_session_timeout_seconds=120) 
        for params in trader_mcp_server_params
        ]
    mcp_servers = trader_mcp_servers + researcher_mcp_servers
    print(f"\n📊 Number of MCP Servers: {len(mcp_servers)}")
  
    # And now for our researcher
    research_question = "What's the latest news on Amazon?"

    for server in researcher_mcp_servers:
        await server.connect()
    researcher = await get_researcher(researcher_mcp_servers)
    with trace("Researcher"):
        result = await Runner.run(researcher, research_question, max_turns=30)
    print_result(result)

    ed_initial_strategy = "You are a day trader that aggressively buys and sells shares based on news and market conditions."
    Account.get("Ed").reset(ed_initial_strategy)

    print_result(await read_accounts_resource("Ed"))
    print_result(await read_strategy_resource("Ed"))

    # And now - to create our Trader Agent
    agent_name = "Ed"

    # Using MCP Servers to read resources
    account_details = await read_accounts_resource(agent_name)
    strategy = await read_strategy_resource(agent_name)

    instructions = f"""
    You are a trader that manages a portfolio of shares. Your name is {agent_name} and your account is under your name, {agent_name}.
    You have access to tools that allow you to search the internet for company news, check stock prices, and buy and sell shares.
    Your investment strategy for your portfolio is:
    {strategy}
    Your current holdings and balance is:
    {account_details}
    You have the tools to perform a websearch for relevant news and information.
    You have tools to check stock prices.
    You have tools to buy and sell shares.
    You have tools to save memory of companies, research and thinking so far.
    Please make use of these tools to manage your portfolio. Carry out trades as you see fit; do not wait for instructions or ask for confirmation.
    """

    prompt = """
    Use your tools to make decisions about your portfolio.
    Investigate the news and the market, make your decision, make the trades, and respond with a summary of your actions.
    """

    print(instructions)

    for server in mcp_servers:
        await server.connect()

    researcher_tool = await get_researcher_tool(researcher_mcp_servers)
    trader = Agent(
        name=agent_name,
        instructions=instructions,
        tools=[researcher_tool],
        mcp_servers=trader_mcp_servers,
        model="gpt-4o-mini",
    )
    with trace(agent_name):
        result = await Runner.run(trader, prompt, max_turns=30)
    print_result(result)

    await read_accounts_resource(agent_name)
    trader = Trader("Ed")
    await trader.run()
    await read_accounts_resource("Ed")
    all_params = trader_mcp_server_params + researcher_mcp_server_params("ed")

    count = 0
    for each_params in all_params:
        async with MCPServerStdio(params=each_params, client_session_timeout_seconds=60) as server:
            mcp_tools = await server.list_tools()
            count += len(mcp_tools)
    print(f"We have {len(all_params)} MCP servers, and {count} tools")

    for param in all_params:
        print(param)
    # return "Test"

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
