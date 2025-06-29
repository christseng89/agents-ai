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
from IPython.display import display, Markdown
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost

# from dotenv import load_dotenv

# load_dotenv(override=True)

ALL_IN_ONE_WORKER = False

@dataclass
class Message:
    content: str


serper = GoogleSerperAPIWrapper()
langchain_serper =Tool(name="internet_search", func=serper.run, description="Useful for when you need to search the internet")
autogen_serper = LangChainToolAdapter(langchain_serper)

instruction1 = "To help with a decision on whether to use AutoGen in a new AI Agent project, \
please research and briefly respond with reasons in favor of choosing AutoGen; the pros of AutoGen."

instruction2 = "To help with a decision on whether to use AutoGen in a new AI Agent project, \
please research and briefly respond with reasons against choosing AutoGen; the cons of Autogen."

judge = "You must make a decision on whether to use AutoGen for a project. \
Your research team has come up with the following reasons for and against. \
Based purely on the research from your team, please respond with your decision and brief rationale."

class Player1Agent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        self._delegate = AssistantAgent(name, model_client=model_client, tools=[autogen_serper], reflect_on_tool_use=True)

    @message_handler
    async def handle_my_message_type(self, message: Message, ctx: MessageContext) -> Message:
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        return Message(content=response.chat_message.content)
    
class Player2Agent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        self._delegate = AssistantAgent(name, model_client=model_client, tools=[autogen_serper], reflect_on_tool_use=True)

    @message_handler
    async def handle_my_message_type(self, message: Message, ctx: MessageContext) -> Message:
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        return Message(content=response.chat_message.content)
    
class Judge(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        self._delegate = AssistantAgent(name, model_client=model_client)
        
    @message_handler
    async def handle_my_message_type(self, message: Message, ctx: MessageContext) -> Message:
        message1 = Message(content=instruction1)
        message2 = Message(content=instruction2)
        inner_1 = AgentId("player1", "default")
        inner_2 = AgentId("player2", "default")
        response1 = await self.send_message(message1, inner_1)
        response2 = await self.send_message(message2, inner_2)
        result = f"## Pros of AutoGen:\n{response1.content}\n\n## Cons of AutoGen:\n{response2.content}\n\n"
        judgement = f"{judge}\n{result}Respond with your decision and brief explanation"
        message = TextMessage(content=judgement, source="user")
        response = await self._delegate.on_messages([message], ctx.cancellation_token)
        return Message(content=result + "\n\n## Decision:\n\n" + response.chat_message.content)

async def main():
    if ALL_IN_ONE_WORKER:

        worker = GrpcWorkerAgentRuntime(host_address="localhost:50051")
        await worker.start()

        await Player1Agent.register(worker, "player1", lambda: Player1Agent("player1"))
        await Player2Agent.register(worker, "player2", lambda: Player2Agent("player2"))
        await Judge.register(worker, "judge", lambda: Judge("judge"))

        agent_id = AgentId("judge", "default")

    else:

        worker1 = GrpcWorkerAgentRuntime(host_address="localhost:50051")
        await worker1.start()
        await Player1Agent.register(worker1, "player1", lambda: Player1Agent("player1"))

        worker2 = GrpcWorkerAgentRuntime(host_address="localhost:50051")
        await worker2.start()
        await Player2Agent.register(worker2, "player2", lambda: Player2Agent("player2"))

        worker = GrpcWorkerAgentRuntime(host_address="localhost:50051")
        await worker.start()
        await Judge.register(worker, "judge", lambda: Judge("judge"))
        agent_id = AgentId("judge", "default")

    response = await worker.send_message(Message(content="Go!"), agent_id)
    display(Markdown(response.content))

    await worker.stop()
    if not ALL_IN_ONE_WORKER:
        await worker1.stop()
        await worker2.stop()

if __name__ == "__main__":
    host = GrpcWorkerAgentRuntimeHost(address="localhost:50051")
    host.start() 
    
    # Run the main function in the event loop
    asyncio.run(main())
    host.stop()
