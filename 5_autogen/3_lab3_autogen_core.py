import asyncio

from dataclasses import dataclass

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient

from autogen_core import AgentId, MessageContext, RoutedAgent, message_handler
from autogen_core import SingleThreadedAgentRuntime
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage

# from rich.console import Console
# from rich.markdown import Markdown

# Initialize Rich console
# console = Console()
# JUDGE = "You are judging a game of rock, paper, scissors. The players have made these choices:\n"
JUDGE = "你正在判断一场石头、剪刀、布的比赛。规则如下：石头赢剪刀，剪刀赢布，布赢石头。玩家的选择如下：\n"


@dataclass
class Message:
    content: str

# Gpt-4o-mini
class PlayerGptAgent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=1.0)
        self._delegate = AssistantAgent(name, model_client=model_client)

    @message_handler
    async def handle_message(self, message: Message, ctx: MessageContext) -> Message:
        # print (f"PlayerGptAgent received message: {message.content}")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        # print (f"PlayerGptAgent response: {response.chat_message.content}")
        return Message(content=response.chat_message.content)

# Llama3.2
class PlayerLlamaAgent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OllamaChatCompletionClient(model="llama3.2", temperature=1.0)
        self._delegate = AssistantAgent(name, model_client=model_client)

    @message_handler
    async def handle_message(self, message: Message, ctx: MessageContext) -> Message:
        # print (f"PlayerLlamaAgent received message: {message.content}")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        # print (f"PlayerLlamaAgent response: {response.chat_message.content}")
        return Message(content=response.chat_message.content)

class RockPaperScissorsAgent(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=1.0)
        self._delegate = AssistantAgent(name, model_client=model_client)

    @message_handler
    async def handle_message(self, message: Message, ctx: MessageContext) -> Message:

        # This is a simple game of rock, paper, scissors between two agents.
        # Each agent will respond with one of the three choices.
        # The judge will determine the winner based on the choices made by the agents.
        # The game is played in a single round, and the result is returned as a message

        agent_1 = AgentId("player1", "default")
        agent_2 = AgentId("player2", "default")
        agent_3 = AgentId("player3", "default")

        # instruction = "You are playing rock, paper, scissors. Respond only with the one word, one of the following randomly: rock, paper, or scissors."
        instruction = "你正在玩石头、剪刀、布游戏。只用一个词回应，随机选择以下三个之一：石头、剪刀或布。"
        message = Message(content=instruction)

        response1 = await self.send_message(message, agent_1)
        response2 = await self.send_message(message, agent_2)
        response3 = await self.send_message(message, agent_3)
        result = f"Player 1: {response1.content}\nPlayer 2: {response2.content}\nPlayer 3: {response3.content}\n    "

        judge = f"{JUDGE}{result}Who wins?"
        message = TextMessage(content=judge, source="user")
        response = await self._delegate.on_messages([message], ctx.cancellation_token)
        return Message(content=result + '\nJudge: ' + response.chat_message.content)

async def main():
    print("Game starting...\n")

    # single_agent is a runtime that allows agents to communicate and interact.
    # It can be thought of as a single-threaded environment where agents can send and receive
    single_agent = SingleThreadedAgentRuntime()

    # Registering agents
    await PlayerGptAgent.register(
        single_agent,
        "player1", 
        lambda: PlayerGptAgent("player1")
    )

    await PlayerLlamaAgent.register(
        single_agent, 
        "player2", 
        lambda: PlayerLlamaAgent("player2")
    )

    await PlayerLlamaAgent.register(
        single_agent, 
        "player3", 
        lambda: PlayerLlamaAgent("player3")
    )

    await RockPaperScissorsAgent.register(
        single_agent, 
        "rock_paper_scissors", 
        lambda: RockPaperScissorsAgent("rock_paper_scissors")
    )

    # Start the single agent runtime
    single_agent.start()
    agent_id = AgentId("rock_paper_scissors", "default")
    message = Message(content="go")
    response = await single_agent.send_message(message, agent_id)
    print(response.content)

    await single_agent.stop()
    await single_agent.close()

if __name__ == "__main__":
    asyncio.run(main())
    