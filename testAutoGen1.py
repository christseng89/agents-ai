import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

async def main() -> None:
    # First concept: the Model
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    # Second concept: the Agent
    agent = AssistantAgent("assistant", model_client=model_client)
    response = await agent.run(task="Say 'Hello World!'")
    # print(f"\nResponse:  {response}")
    for m in response.messages:
        if m.source == 'assistant':
            print(f"\nResponse content:  {m.content}")

    agent2 = AssistantAgent(
        name="airline_agent",
        model_client=model_client,
        system_message="You are a helpful assistant for an airline. You give short, humorous answers.",
        model_client_stream=True
    )
    message = TextMessage(content="I'd like to go to London", source="user")
    response = await agent2.on_messages([message], cancellation_token=CancellationToken())
    print(f"\nResponse message: {response.chat_message.content}")
    
    await model_client.close()

asyncio.run(main())