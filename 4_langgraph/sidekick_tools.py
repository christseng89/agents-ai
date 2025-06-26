from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
import os
import requests
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

from langchain.tools import tool
import subprocess

load_dotenv(override=True)
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"
serper = GoogleSerperAPIWrapper()

async def playwright_tools():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright


def pushover(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
    return "success"


def get_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()

@tool
def js_eval(code: str) -> str:
    """Execute JavaScript code using Node.js and return the output"""
    try:
        with open("temp_code.js", "w", encoding="utf-8") as f:
            f.write(code)
        result = subprocess.run(["node", "temp_code.js"], capture_output=True, timeout=5, text=True)
        return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
    except Exception as e:
        return f"JavaScript execution error: {e}"

async def more_tools():
    pushover_tool = Tool(name="send_push_notification", func=pushover, description="Use this tool when you want to send a push notification")
    file_tools = get_file_tools()

    serper_tool =Tool(
        name="search",
        func=serper.run,
        description="Use this tool when you want to get the results of an online web search"
    )

    wikipedia = WikipediaAPIWrapper()
    wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)

    python_repl = PythonREPLTool()
    
    js_eval_tool = Tool(
        name="javascript_executor",  # ✅ 合法名稱，符合 regex: ^[a-zA-Z0-9_-]+$
        func=js_eval,
        description="Execute JavaScript code snippets. Input should be valid JS expression or script."
    )

    return file_tools + [pushover_tool, serper_tool, js_eval_tool, python_repl,  wiki_tool ]
