from playwright.sync_api import sync_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
import threading

def run_sync_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=browser)  # ✅ Fixed
        tools = toolkit.get_tools()
        print("✅ Loaded tools:", tools)

thread = threading.Thread(target=run_sync_browser)
thread.start()
thread.join()
