#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This script sets up and runs a financial agent system with MCP servers for research and trading.

import os
import sys
import asyncio

from dotenv import load_dotenv
from agents import Agent, Runner, trace, Tool
from agents.mcp import MCPServerStdio

from datetime import datetime
from contextlib import AsyncExitStack
from accounts_client import read_accounts_resource, read_strategy_resource
from accounts import Account
from traders import Trader # A python class that manages trading operations
from reset import reset_traders
from mcp_params import researcher_mcp_server_params, trader_mcp_server_params
from templates import get_trader_instructions

from result_utils import print_result, print_tools

# Load environment variables from a .env file
load_dotenv(override=True)

# Retrieve Polygon API key and plan from environment variables
polygon_api_key = os.getenv("POLYGON_API_KEY")
polygon_plan = os.getenv("POLYGON_PLAN")

# Determine if the Polygon plan is 'paid' or 'realtime'
is_paid_polygon = polygon_plan == "paid"
is_realtime_polygon = polygon_plan == "realtime"

# Print the current Polygon plan status
print("is_paid_polygon:", is_paid_polygon)
print("is_realtime_polygon:", is_realtime_polygon)

# Define researcher MCP parameters with Brave API key
brave_env = {
    "BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")
}

# List of MCP server parameters for researcher and trader
mcp_server_params = [
    {"command": "uvx", "args": ["mcp-server-fetch"]},
    {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-brave-search"], "env": brave_env}
]

prompt = """
Use your tools to make decisions about your portfolio.
Investigate the news and the market, make your decision, make the trades, and respond with a summary of your actions.
"""

accounts_name = "Ed"
research_question = "What's the latest news on Amazon?"

# Function to create a researcher agent with specific instructions
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

# Function to wrap the researcher agent as a tool
async def get_researcher_tool(mcp_servers) -> Tool:
    researcher = await get_researcher(mcp_servers)
    return researcher.as_tool(
        tool_name="Researcher",
        tool_description=(
            "This tool researches online for news and opportunities, either based on your specific request "
            "to look into a certain stock, or generally for notable financial news and opportunities. "
            "Describe what kind of research you're looking for."
        )
    )

async def print_mcp_servers(type, mcp_servers):
    # Confirm tools are loaded for each server
    print(f"\n🔍 {type} MCP Servers with {len(mcp_servers)} servers:\n")
    for idx, server in enumerate(mcp_servers, 1):
        tools = await server.list_tools()
        print(f"\n✅ {type} Server {idx}, with {len(tools)} tools")
        print_tools(tools)

# Main asynchronous function to run the agent system
async def main():    
    # AsyncExitStack => Context stack ensures proper 'cleanup' of resources
    async with AsyncExitStack() as stack:
        # Initialize Researcher MCP servers
        researcher_mcp_servers = []
        for params in mcp_server_params:
            server = MCPServerStdio(
                params,
                client_session_timeout_seconds=300,
            )
            await stack.enter_async_context(server)
            researcher_mcp_servers.append(server)

        await print_mcp_servers("Researcher", researcher_mcp_servers)

        # Initialize Trader MCP servers
        trader_mcp_servers = []
        for params in trader_mcp_server_params: # accounts_server.py, push_server.py, and market_server.py
            server = MCPServerStdio(
                params,
                client_session_timeout_seconds=300,
            )
            await stack.enter_async_context(server)
            trader_mcp_servers.append(server)

        await print_mcp_servers("Trader", trader_mcp_servers)

        # Combine all MCP servers for reference ONLY
        # This is not used in the agent, but can be useful for debugging or logging
        combined_mcp_servers = trader_mcp_servers + researcher_mcp_servers
        print(f"\n📊 Number of MCP Servers: {len(combined_mcp_servers)}")

        # Run researcher agent to gather information
        researcher = await get_researcher(researcher_mcp_servers)
        with trace("Researcher"):
            result = await Runner.run(researcher, research_question, max_turns=30)
        print_result(result)

        # Reset trader account with initial strategy
        ed_initial_strategy = (
            "You are a day trader that aggressively buys and sells shares based on news and market conditions."
        )
        Account.get(accounts_name).reset(ed_initial_strategy)
        print_result(await read_accounts_resource(accounts_name))
        print_result(await read_strategy_resource(accounts_name))

        # Set up trader agent with specific instructions
        agent_name = accounts_name
        print(f"\nSetting up trader agent: {agent_name}")
        instructions = await get_trader_instructions(agent_name)
        researcher_tool = await get_researcher_tool(researcher_mcp_servers)

        # Initialize trader agent
        # Using external Researcher MCP servers for tools
        # Using owner Trader MCP servers for trading
        print(f"\n🚀 Initializing Trader Agent: {agent_name}")

        trader = Agent(
            name=agent_name,
            instructions=instructions,
            tools=[researcher_tool],  # 👈 Use Researcher as a tool
            mcp_servers=trader_mcp_servers,  # 👈 Use Trader MCP servers only
            model="gpt-4o-mini",
        )

        # Run the trader agent
        with trace(agent_name):
            result = await Runner.run(trader, prompt, max_turns=30)
        print_result(result)
        await read_accounts_resource(agent_name)

        # Initialize and run trader object
        print(f"\n🔄 Running Trader Object for {agent_name}")
        trader_obj = Trader(agent_name)
        await trader_obj.run()
        print_result(await read_accounts_resource(agent_name))

        # Check all MCP tools for each server
        # For debugging purposes, we can list all tools available in each MCP server
        print("\n🔧 Listing all MCP tools from all servers:")
        all_params = trader_mcp_server_params + researcher_mcp_server_params(agent_name.lower)

        count = 0
        for each_params in all_params:
            async with MCPServerStdio(
                params=each_params,
                client_session_timeout_seconds=60,
            ) as server:
                mcp_tools = await server.list_tools()
                count += len(mcp_tools)
        print(f"\n\nWe have {len(all_params)} MCP servers, and {count} tools\n")

        for params in all_params:
            print(f"Params: {params}")

        print_tools(mcp_tools)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    asyncio.run(main())
    sys.exit(0)
