import json
import openai


# ------------------ TOOL FUNCTIONS ------------------
def say_hello(name: str):
    return {"greeting": f"Hello, {name}!"}

def add(a: int, b: int):
    return {"sum": a + b}

# ------------------ TOOL DEFINITIONS ------------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "say_hello",
            "description": "Return a friendly greeting",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two integers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    }
]

# ------------------ SYSTEM PROMPT ------------------
system_prompt = """
You are a helpful assistant that can call tools like 'say_hello' and 'add' when appropriate.
Use tools when necessary to help the user.
"""

# ------------------ TOOL CALL HANDLER ------------------
def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name} with {arguments}", flush=True)
        tool = globals().get(tool_name)
        result = tool(**arguments) if tool else {}
        results.append({
            "role": "tool",
            "content": json.dumps(result),
            "tool_call_id": tool_call.id
        })
    return results

# ------------------ CHAT FUNCTION ------------------
def chat(message, history):
    messages = (
        [{"role": "system", "content": system_prompt}]
        + history
        + [{"role": "user", "content": message}]
    )
    done = False
    while not done:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4" if needed
            messages=messages,
            tools=tools
        )
        finish_reason = response.choices[0].finish_reason

        if finish_reason == "tool_calls":
            message_from_llm = response.choices[0].message
            tool_calls = message_from_llm.tool_calls
            print("LLM requested tool calls:", flush=True)
            for i, tool_call in enumerate(tool_calls, 1):
                print(f"  [{i}] Tool Name: {tool_call.function.name}", flush=True)
                print(f"      Arguments: {tool_call.function.arguments}", flush=True)
                print(f"      Tool Call ID: {tool_call.id}", flush=True)

            print("\n🧰 Calling tools...\n", flush=True)
            results = handle_tool_calls(tool_calls)
            messages.append(message_from_llm)
            messages.extend(results)
        else:
            done = True

    return response.choices[0].message.content

# ------------------ MAIN ------------------
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv(override=True)

    openai_api_key = os.getenv('OPENAI_API_KEY')

    print("\n🛠️ Available Tools:", flush=True)
    for i, tool in enumerate(tools, 1):
        print(f"  [{i}] 🔧 {tool['function']['name']} - {tool['function'].get('description', 'No description')}", flush=True)
    print("\n")

    conversation_history = []  # Optional: keep full conversation
    user_input = "Add 15 and 27, then greet Charlie."

    reply = chat(user_input, conversation_history)
    print("\n")
    print("💬 User input:", user_input)
    print("✅ Assistant reply:", reply)
