import os
import requests
import asyncio
from dataclasses import dataclass
from autogen_core import AgentId, MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.langchain import LangChainToolAdapter
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntime
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost

from rich.console import Console
from rich.markdown import Markdown

# Initialize Rich console
console = Console()
ALL_IN_ONE_WORKER = True
HOST_ADDRESS = "localhost:50051"
PRODUCT2 = "CrewAI"
PRODUCT1 = "Microsoft AutoGen"
PRODUCT3 = "LangGraph"

# Structured data

@dataclass
class Message:
    content: str


def pushover(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
    return "success"

pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"
langchain_pushover = Tool(name="send_push_notification", func=pushover, description="Use this tool when you want to send a push notification")
pushover_tool = LangChainToolAdapter(langchain_pushover)

serper = GoogleSerperAPIWrapper()
langchain_serper =Tool(name="internet_search", func=serper.run, description="Useful for when you need to search the internet")
serper_tool = LangChainToolAdapter(langchain_serper)


instruction1 = f"To help with a decision on either to use {PRODUCT1}, {PRODUCT2}, or {PRODUCT3} in a new AI Agent project, \
please research and briefly respond with reasons in favor of choosing {PRODUCT1}, {PRODUCT2}, and {PRODUCT3}; the pros of {PRODUCT1}, {PRODUCT2}, and {PRODUCT3}."

instruction2 = f"To help with a decision on either to use {PRODUCT1}, {PRODUCT2}, or {PRODUCT3} in a new AI Agent project, \
please research and briefly respond with reasons against choosing {PRODUCT1}, {PRODUCT2}, and {PRODUCT3}; the cons of {PRODUCT1}, {PRODUCT2}, and {PRODUCT3}."

judge = f"""As an AI Agent expert, you must decide whether to use {PRODUCT1}, {PRODUCT2}, or {PRODUCT3} for a new AI project.
Your research team has provided reasons for and against.
Based on the team’s research, respond with your professional decision and brief rationale.
After generating your response, also send a notification to the user with a brief summary of your decision.
"""

class PlayerGpt4oMiniAgent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        self._delegate = AssistantAgent(name, model_client=model_client, tools=[serper_tool], reflect_on_tool_use=True)

    @message_handler
    async def handle_my_message_type(self, message: Message, ctx: MessageContext) -> Message:
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        return Message(content=response.chat_message.content)
    
class PlayerGpt4oAgent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        self._delegate = AssistantAgent(name, model_client=model_client, tools=[serper_tool], reflect_on_tool_use=True)

    @message_handler
    async def handle_my_message_type(self, message: Message, ctx: MessageContext) -> Message:
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        return Message(content=response.chat_message.content)
    
class Judge(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        self._delegate = AssistantAgent(name, model_client=model_client, tools=[pushover_tool], )
        
    @message_handler
    async def handle_my_message_type(self, message: Message, ctx: MessageContext) -> Message:
        message1 = Message(content=instruction1)
        message2 = Message(content=instruction2)
        
        agent_1 = AgentId("player1", "default")
        agent_2 = AgentId("player2", "default")
        response1 = await self.send_message(message1, agent_1)
        response2 = await self.send_message(message2, agent_2)

        result = f"## Pros of AutoGen:\n{response1.content}\n\n## Cons of AutoGen:\n{response2.content}\n\n"
        judgement = f"{judge}\n{result}Respond with your decision and brief explanation"
        message = TextMessage(content=judgement, source="user")
        response = await self._delegate.on_messages([message], ctx.cancellation_token)
        return Message(content=result + "\n\n## Decision:\n\n" + response.chat_message.content)

async def main():
    print(f"Starting distributed agents for {PRODUCT1}, {PRODUCT2}, and {PRODUCT3}...")
    if ALL_IN_ONE_WORKER:
        worker = GrpcWorkerAgentRuntime(host_address=HOST_ADDRESS)
        await worker.start()

        await PlayerGpt4oMiniAgent.register(worker, "player1", lambda: PlayerGpt4oMiniAgent("player1"))
        await PlayerGpt4oAgent.register(worker, "player2", lambda: PlayerGpt4oAgent("player2"))
        await Judge.register(worker, "judge", lambda: Judge("judge"))

        agent_id = AgentId("judge", "default")

    else:
        worker1 = GrpcWorkerAgentRuntime(host_address=HOST_ADDRESS)
        await worker1.start()
        await PlayerGpt4oMiniAgent.register(worker1, "player1", lambda: PlayerGpt4oMiniAgent("player1"))

        worker2 = GrpcWorkerAgentRuntime(host_address=HOST_ADDRESS)
        await worker2.start()
        await PlayerGpt4oAgent.register(worker2, "player2", lambda: PlayerGpt4oAgent("player2"))
        # await PlayerGpt4oMiniAgent.register(worker2, "player2", lambda: PlayerGpt4oMiniAgent("player2"))

        worker = GrpcWorkerAgentRuntime(host_address=HOST_ADDRESS)
        await worker.start()
        await Judge.register(worker, "judge", lambda: Judge("judge"))
        agent_id = AgentId("judge", "default")

    response = await worker.send_message(Message(content="Go!"), agent_id)
    # display(Markdown(response.content))
    console.print(Markdown(response.content))

    # Stop workers ...
    await worker.stop()
    if not ALL_IN_ONE_WORKER:
        await worker1.stop()
        await worker2.stop()

async def main_wrapper():
    host = GrpcWorkerAgentRuntimeHost(address=HOST_ADDRESS)
    # Call without await
    host.start()  # synchronous method, no await needed here
    try:
        await main()
    finally:
        await host.stop()  

if __name__ == "__main__":
    asyncio.run(main_wrapper())
