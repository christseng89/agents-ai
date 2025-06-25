from langchain_community.tools.playwright.utils import create_async_playwright_browser
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
import asyncio
import nest_asyncio

nest_asyncio.apply()  # ✅ Allows nested asyncio.run

async def test_browser():
    browser = create_async_playwright_browser(headless=True)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    navigate_tool = [t for t in toolkit.get_tools() if t.name == "navigate_browser"][0]
    result = await navigate_tool.arun({"url": "https://www.xe.com"})
    print(result)

asyncio.run(test_browser())
