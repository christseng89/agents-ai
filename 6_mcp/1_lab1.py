from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
import os
import asyncio


load_dotenv(override=True)

async def main():
    print("Starting MCP Server for Fetch...")
    fetch_params = {"command": "uvx", "args": ["mcp-server-fetch"]}
    async with MCPServerStdio(params=fetch_params, client_session_timeout_seconds=100) as server:
        fetch_tools = await server.list_tools()

    # fetch_tools
    print (f"Tools length: {len(fetch_tools)}\n")
    for tool in fetch_tools:
        print (f"Tool name: '{tool.name}', Description: '{tool.description}'")

    print("\nStarting MCP Server for Playwright...")
    playwright_params = {"command": "npx","args": [ "@playwright/mcp@latest"]}
    async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=100) as server:
        playwright_tools = await server.list_tools()

    # playwright_tools
    print (f"Tools length: {len(playwright_tools)}\n")
    for tool in playwright_tools:
        print (f"Tool name: '{tool.name}', Description: '{tool.description}'")

    print("\nStarting MCP Server for Filesystem...")
    sandbox_path = os.path.abspath(os.path.join(os.getcwd(), "sandbox"))
    files_params = {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", sandbox_path]}
    async with MCPServerStdio(params=files_params,client_session_timeout_seconds=100) as server:
        file_tools = await server.list_tools()

    # file_tools
    print (f"Tools length: {len(file_tools)}\n")
    for tool in file_tools:
        print (f"Tool name: '{tool.name}', Description: '{tool.description[:50]}'")

    instructions = """
    Use internet search tools to find the information you need—do not open a browser or manually click links.
    Leverage the search API to access multiple sources, read summaries, and extract key details.
    If one result isn't helpful, try different queries or results.
    Continue searching and refining until you fully complete the assignment.
    """

    food_menu = "Guinness Beef Stew"
    message = f"Find a great recipe for {food_menu}, then summarize it in markdown to {food_menu.lower().replace(" ", "_")}-recipe.md in the sandbox directory."

    async with MCPServerStdio(params=files_params, client_session_timeout_seconds=100) as mcp_server_files:
        async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=100) as mcp_server_browser:
            print ("\nStarting Investigator Agent...")
            agent = Agent(
                name="investigator", 
                instructions=instructions, 
                model="gpt-4.1-mini",
                mcp_servers=[mcp_server_files, mcp_server_browser]
                )
            with trace("investigate"):
                result = await Runner.run(agent, message)
                print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    
