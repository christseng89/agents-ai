# openai_date_tool.py

import asyncio
from openai import OpenAI
import json
from date_client import call_get_today_date
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI()

functions = [
    {
        "name": "get_today_date",
        "description": "Returns today's date in YYYY-MM-DD format.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]

async def main():
    completion = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is today's date?"}
        ],
        functions=functions
    )

    message = completion.choices[0].message

    if message.function_call:
        print(f"LLM calls function: '{message.function_call.name}'")

    # Call MCP tool
    result = await call_get_today_date()

    followup = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is today's date?"},
            {
                "role": "function",
                "name": message.function_call.name,
                "content": json.dumps(result)
            }
        ]
    )

    print(followup.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(main())
