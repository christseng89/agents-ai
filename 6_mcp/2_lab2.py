from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
from accounts import Account
from accounts_client import (
    get_accounts_tools_openai,
    read_accounts_resource,
    list_accounts_tools
)
import asyncio
import json
import random

load_dotenv(override=True)

def print_account_info(account):
    """
    Prints a summary of the given account object.
    """

    print(f"Name: {account.name}")
    print(f"Balance: ${account.balance:.2f}")

    strategy_short = account.strategy
    if len(strategy_short) > 60:
        strategy_short = strategy_short[:60] + "..."
    print(f"Strategy: {strategy_short}\n")

    print("📊 === HOLDINGS ===")
    for symbol, qty in account.holdings.items():
        print(f"  {symbol}: {qty} shares")
    print()

    print("💰 === PORTFOLIO VALUE ===")
    if account.portfolio_value_time_series:
        latest_time, latest_value = account.portfolio_value_time_series[-1]
        print(f"Latest portfolio value: ${latest_value:.2f} at {latest_time}")
    else:
        print("No portfolio value time series data available.")

def print_account_summary(context):
    """
    Prints a formatted summary of an account given its context dictionary.
    """
    print("\n✅ === ACCOUNT SUMMARY ===")
    print(f"Name: {context['name']}")
    print(f"Balance: ${context['balance']:.2f}")
    print(f"Strategy: {context['strategy']}\n")

    print("📊 === HOLDINGS ===")
    for symbol, qty in context["holdings"].items():
        print(f"  {symbol}: {qty} shares")
    print()

    print("📝 === TRANSACTIONS ===")
    for tx in context["transactions"]:
        action = "BUY" if tx["quantity"] > 0 else "SELL"
        quantity = abs(tx["quantity"])
        print(f"- [{tx['timestamp']}] {action} {quantity} {tx['symbol']} @ ${tx['price']:.2f}")
        print(f"    Rationale: {tx['rationale']}\n")

    print("💰 === PORTFOLIO VALUE ===")
    print(f"Total Value: ${context['total_portfolio_value']:.2f}")
    print(f"Total Profit/Loss: ${context['total_profit_loss']:.2f}")

async def main():
    # -------------------------------
    # Accounts Operations
    # -------------------------------
    account = Account.get("Ed")
    # -------------------------------
    # PRINT IMPORTANT INFORMATION
    # -------------------------------

    print_account_info(account)

    amount = random.randint(500, 2000)
    account.deposit(amount)
    print(f"\nDeposit of ${amount:,.2f} completed. New balance: ${account.balance:,.2f}.\n")
    account.buy_shares("AMZN", random.randint(1, 3), "Because this bookstore website looks promising")
    account.buy_shares("NVDA", random.randint(1, 2), "Because its AI chips technology looks promising")

    account.report()
    account.list_transactions()

    # -------------------------------
    # Start MCP Server
    # -------------------------------
    print("Starting MCP Server for Accounts...")
    params = {"command": "uv", "args": ["run", "accounts_server.py"]} # uv run accounts_server.py
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        server_tools = await server.list_tools()

    print("\n🤖 List of Tools - Accounts Server:\n" + "="*40)
    for tool in server_tools:
        print(f"\nName: '{tool.name}' \nDescription: '{tool.description}'")    

    # -------------------------------
    # Agent MCP Server
    # -------------------------------
    instructions = "You are able to manage an account for a client, and answer questions about the account."
    request = "My name is Ed and my account is under the name Ed. What's my balance and my holdings?"
    model = "gpt-4.1-mini"

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(
            name="account_manager",
            instructions=instructions,
            model=model,
            mcp_servers=[mcp_server]
        )
        with trace("account_manager"):
            result = await Runner.run(agent, request)
        print(result.final_output)

    # -------------------------------
    # Account Client Tools 
    # -------------------------------
    client_server_tools = await list_accounts_tools() # Exposed accounts server tools to accounts client
    for tool in client_server_tools:
        print(f"\nName: '{tool.name}' \nDescription: '{tool.description}'")    
        
    client_openai_tools = await get_accounts_tools_openai() # Convert tools to OpenAI Tool -> FunctionTool
    print("\n🤖 List of OpenAI Tools - Accounts Client:\n" + "="*40)
    for tool in client_openai_tools:
        print(f"\nName: '{tool.name}' \nDescription: '{tool.description}'")

    # -------------------------------
    # Agent with OpenAI tools
    # -------------------------------
    request = "My name is Ed and my account is under the name Ed. What's my balance?"

    agent = Agent(
        name="account_manager",
        instructions=instructions,
        model=model,
        tools=client_openai_tools
    )
    with trace("account_mcp_client"):
        result = await Runner.run(agent, request)
        print(result.final_output)

    # -------------------------------
    # Read account resource
    # -------------------------------
    context = await read_accounts_resource("ed")
    context = json.loads(context)
    # print("Account context:", context)

    print_account_summary(context)
    Account.get("Ed").report()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Shutdown requested — exiting…")  

