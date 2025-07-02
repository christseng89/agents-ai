from mcp.server.fastmcp import FastMCP
from market import get_share_price, get_share_price_polygon_eod

mcp = FastMCP("market_server")

@mcp.tool()
async def lookup_share_price(symbol: str) -> float:
    """This tool provides the current price of the given stock symbol.

    Args:
        symbol: the symbol of the stock
    """
    return get_share_price(symbol)

@mcp.tool()
async def lookup_share_price_polygon_eod(symbol: str) -> float:
    """This tool provides the end-of-day price of the given stock symbol using Polygon.io.

    Args:
        symbol: the symbol of the stock
    """
    return get_share_price_polygon_eod(symbol)

@mcp.tool()
async def get_available_symbols() -> list[str]:
    """This tool returns a list of available stock symbols."""
    return ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

if __name__ == "__main__":
    mcp.run(transport='stdio')