import asyncio
from dotenv import load_dotenv
from agents.mcp import MCPServerStdio
from agents import Agent, Runner, trace

load_dotenv()

async def main():
    params = {
        "command": "uvx",
        "args": ["awslabs.aws-documentation-mcp-server@latest"],
        "env": {
            "FASTMCP_LOG_LEVEL": "ERROR",
            "AWS_DOCUMENTATION_PARTITION": "aws"
        },
        "disabled": False,
        "autoApprove": []
    }

    try:
        print("🔄 Starting AWS MCP Server...")
        async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
            print("✅ AWS MCP Server is running.")

            # Get all tools from MCP server
            tools = await server.list_tools()
            print("✅ Available tools:")
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")

            # Initialize Agent with tools (FIXED tools assignment)
            agent = Agent(
                name="aws-doc-agent",
                mcp_servers=[server],
                instructions="You are an expert in AWS documentation. Use the tools provided to answer questions about AWS services and configurations.",
                model="gpt-4o-mini",
                # tools=tools  # ✅ FIXED HERE
            )

            question = "How do I configure Amazon S3 with Python using Boto3?"
            print(f"\n🤖 Asking Agent: {question}\n")

            # Optional trace for debugging conversation flow
            print("🔍 Waiting for Answers..")
            with trace("aws-doc-agent"):
                response = await Runner.run(agent, question, max_turns=20)

            print("📘 Agent Response:\n", response)

    except Exception as e:
        print("❌ Error during execution:", str(e))


if __name__ == "__main__":
    asyncio.run(main())
