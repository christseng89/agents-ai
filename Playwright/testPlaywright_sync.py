# testPlaywright_async.py

import asyncio
from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit

async def main():
    print("Loading Sync Playwright Browser Toolkit...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
        tools = toolkit.get_tools()
        print(f"✅ Loaded tools: {tools}")

if __name__ == "__main__":
    asyncio.run(main())
# testPlaywright_sync.py