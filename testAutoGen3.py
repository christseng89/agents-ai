# Patch global input() at the very top to avoid waiting for user input
import builtins
builtins.input = lambda prompt='': "Automated response"


from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer

from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

import asyncio
import os
from autogen_agentchat.agents import UserProxyAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_core import CancellationToken
from autogen_ext.models.openai import _model_info
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

async def main():
    # Set environment variable for prompt mode
    os.environ['PROMPT_MODE'] = 'auto'
    print("PROMPT_MODE =", os.getenv('PROMPT_MODE', 'not set'))
    print("input() patched to always return 'Automated response'")

    # Create model info with structured_output enabled
    model_info = _model_info.ModelInfo(
        endpoint="https://api.anthropic.com/v1/claude",
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        family="claude",
        vision=None,
        function_calling="auto",
        json_output=True,
        structured_output=True
    )

    # Initialize model client
    
    model_client = OpenAIChatCompletionClient(
        model="claude-3-7-sonnet-20250219",
        model_info=model_info,
        timeout=60.0
    )

    # Create user proxy and team
    user_proxy = UserProxyAgent("User")
    team = RoundRobinGroupChat([user_proxy])

    # List of user messages
    user_messages = [
        "Hello, I need help with my bill.",
        "Yes, my latest bill seems incorrect.",
        "Can you explain the charges?"
    ]

    message = (
        "You are a helpful customer service agent. "
        "Respond to the user's queries about their bill in a friendly and professional manner."
    )
    
    # Run conversation with timeout to prevent hang
    for msg in user_messages:
        print(f"\nUser: {msg}")
        try:
            # Wrap in asyncio.wait_for for quick timeout if stuck
            response = await asyncio.wait_for(
                team.run(task=msg, cancellation_token=CancellationToken()), 
                timeout=10  # seconds
            )
            for m in response.messages:
                print(f"{m.source}: {m.content}")
        except asyncio.TimeoutError:
            print("Response timed out: possible prompt or hang.")

    # Close client
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())

