# date_server.py

from mcp.server.fastmcp import FastMCP
from datetime import datetime

# Create MCP server
mcp = FastMCP("date_server")

@mcp.tool()
async def get_today_date() -> str:
    """
    Return today's date in YYYY-MM-DD format.
    """
    return datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    mcp.run(transport='stdio')
