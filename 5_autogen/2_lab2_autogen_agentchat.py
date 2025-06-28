import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.langchain import LangChainToolAdapter
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
from rich.console import Console
from rich.markdown import Markdown

from pydantic import BaseModel, Field
from typing import List

# Structured data
class FlightOffer(BaseModel):
    summary: str = Field(description="Summary of flight")
    airline: str = Field(description="Name of the airline")
    price: str = Field(description="Price of the flight")
    departure_time: str = Field(description="Scheduled departure time")
    arrival_time: str = Field(description="Scheduled arrival time")
    flight_number: str = Field(description="Flight number")
    booking_url: str = Field(description="URL to book the flight")

# Initialize Rich console
console = Console()

# Build your prompt
from_airport = "Taipei"
to_airport = "Paris"
in_date = "July 2025"
prompt = f"""Find a one-way non-stop flight from {from_airport} to {to_airport} in {in_date}."""

# Setup the external tools
serper = GoogleSerperAPIWrapper()
langchain_serper = Tool(name="internet_search", func=serper.run, description="useful for when you need to search the internet")
autogen_serper = LangChainToolAdapter(langchain_serper)

# Initialize the model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# Create the system agents
system_message = (
    "You are a helpful AI research assistant who searches for promising flight deals based on user queries. "
    "After receiving messages or feedback, use your expertise to organize and summarize the information in a professional Markdown format. "
    "Incorporate any feedback provided to refine your responses accordingly."
)
primary_agent = AssistantAgent(
    "primary",
    model_client=model_client,
    tools=[autogen_serper],
    system_message=system_message,
    # output_content_type=FlightOffer,
)

evaluation_agent = AssistantAgent(
    "evaluator",
    model_client=model_client,
    system_message="Provide constructive feedback. Respond with 'APPROVE' when your feedback is addressed.",
)

text_termination = TextMentionTermination("APPROVE")

# Setup the team chat (Round Robin)
team = RoundRobinGroupChat(
    [primary_agent, evaluation_agent], 
    termination_condition=text_termination, 
    max_turns=20
)

# Define an async main() to await team.run()
async def main():
    # Await team.run
    result = await team.run(task=prompt)

    # Display the messages
    for message in result.messages:
        md_text = f"## _**{message.source.capitalize()}**_:\n\n{message.content}"
        console.print(Markdown(md_text))

# Run the async main() loop
if __name__ == "__main__":
    asyncio.run(main())
