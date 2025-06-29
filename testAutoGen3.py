# Patch global input() at the very top to avoid waiting for user input
import builtins
builtins.input = lambda prompt='': "Automated response"

import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.agents import UserProxyAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import _model_info
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

# from dataclasses import dataclass

# AG Core ...
# from autogen_core import AgentId, MessageContext, RoutedAgent, message_handler
# from autogen_core import SingleThreadedAgentRuntime
# from autogen_core import CancellationToken

# from autogen_agentchat.messages import TextMessage
# from autogen_agentchat.ui import Console
# from autogen_ext.agents.web_surfer import MultimodalWebSurfer

load_dotenv()

async def main():
    # Set environment variable for prompt mode
    os.environ['PROMPT_MODE'] = 'auto'
    print("PROMPT_MODE =", os.getenv('PROMPT_MODE', 'not set'))
    print("input() patched to always return 'Automated response'")

    # Model Configuration (Anthropic Claude)
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    if not anthropic_api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment variables.")

    model_info = _model_info.ModelInfo(
        endpoint="https://api.anthropic.com/v1/claude",
        api_key=anthropic_api_key,
        family="claude",
        vision=None,
        function_calling="auto",
        json_output=True,
        structured_output=True
    )

    # Initialize Model Client
    model_client = OpenAIChatCompletionClient(
        model="claude-3-7-sonnet-20250219",
        model_info=model_info,
        timeout=60.0
    )

    # Create Agents
    receptionist_agent = AssistantAgent(
        name="Receptionist",
        system_message="You are a friendly and helpful receptionist. Greet the user and determine if they need help with billing, technical support, or general inquiries.  Then, direct the user to the appropriate agent. Be concise.",
        model_client=model_client
    )

    billing_agent = AssistantAgent(
        name="BillingAgent",
        system_message="You are a billing specialist. Help users with billing questions and issues. Be friendly and professional.",
        model_client=model_client
    )

    tech_support_agent = AssistantAgent(
        name="TechSupportAgent",
        system_message="You are a technical support specialist. Assist users with technical issues and provide solutions. Be clear and helpful.",
        model_client=model_client
    )

    admin_agent = AssistantAgent(
        name="AdminAgent",
        system_message="You are an administrator. Handle general inquiries and requests that do not fall under billing or tech support. Be informative and efficient.",
        model_client=model_client
    )

    # User Proxy Agent
    user_proxy = UserProxyAgent("user_proxy")  
    # termination = TextMentionTermination("exit", sources=["user_proxy"])
    text_termination = TextMentionTermination("APPROVE")

    # Web surfer and user proxy take turns in a round-robin fashion.
    team = RoundRobinGroupChat(
        [receptionist_agent, billing_agent, tech_support_agent, admin_agent, user_proxy], 
        termination_condition=text_termination,
        max_turns=3
    )

    # Example User Messages
    user_messages = [
        "Hello, I need help with my bill.",
        "I am having technical difficulties accessing my account.",
        "I have a general question about your company charges policies.",
        "I need to understand a charge on my bill",
        "My internet is not working",
        "I want to change my password",
        "Exit"  # This will trigger the termination condition
    ]

    try:
        for msg in user_messages:
            print(f"\n\t👤 User: {msg}")
            # Create a TextMessage from the user input
            message = msg
            # Process the message through the team
            response = await team.run(task=message)
            print(f"\n🤖 Response from team:")
            if hasattr(response, 'messages'):
                for m in response.messages:
                    print(f"  📣 Source: {m.source}")
                    print(f"  💬 Content: {m.content}")
            else:
                print("  No messages in response.")

    finally:
        await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
