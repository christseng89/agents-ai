#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from rich.console import Console
from rich.markdown import Markdown

# Create a global Rich console instance
console = Console()

def print_result(result):
    """
    Prints the result from an Agent call or other output.
    Supports either an object with a 'final_output' attribute,
    or a plain string result.
    """
    if result is None:
        console.print(Markdown("⚠️ No result available."))
        return

    if hasattr(result, "final_output"):
        output = result.final_output or "⚠️ Agent returned no output."
        console.print(Markdown(output))
    else:
        print_result_string(result)


def print_result_string(result_string: str):
    """
    Prints a structured JSON result or a plain string result.

    If the string is JSON and matches an account format,
    it prints it nicely formatted. Otherwise it prints
    raw text.
    """
    try:
        data = json.loads(result_string)

        if (
            isinstance(data, dict)
            and "name" in data
            and "balance" in data
            and "strategy" in data
        ):
            print("✅ === ACCOUNT SUMMARY ===")
            print(f"Name: {data['name']}")
            print(f"Balance: ${data['balance']:,.2f}")
            print("Strategy:")
            print(f"  {data['strategy']}")
            print()

            if data.get("holdings"):
                print("📊 === HOLDINGS ===")
                for symbol, qty in data["holdings"].items():
                    print(f"  {symbol}: {qty} shares")
                print()

            if data.get("transactions"):
                print("📝 === TRANSACTIONS ===")
                for tx in data["transactions"]:
                    action = "BUY" if tx["quantity"] > 0 else "SELL"
                    qty = abs(tx["quantity"])
                    price = tx["price"]
                    print(f"- [{tx['timestamp']}] {action} {qty} {tx['symbol']} @ ${price:,.2f}")
                    print(f"    Rationale: {tx['rationale']}")
                print()

            if data.get("total_portfolio_value") is not None:
                print("💰 === PORTFOLIO VALUE ===")
                print(f"Total Portfolio Value: ${data['total_portfolio_value']:,.2f}")
                print(f"Total Profit/Loss: ${data['total_profit_loss']:,.2f}")
                print()

        else:
            print("🔹 JSON Object:\n", json.dumps(data, indent=2))

    except json.JSONDecodeError:
        print("📄 === TEXT RESULT ===")
        print(result_string)
        print()


# Optional: test the module directly
if __name__ == "__main__":
    # Test with dummy string
    print_result_string('{"name": "Ed", "balance": 5000.75, "strategy": "Aggressive trading"}')

    # Test with non-JSON text
    print_result_string("Some plain text result from an agent.")
