from autogen_core import AgentId
import glob
import os


import random

def find_recipient() -> AgentId:
    try:
        agent_files = glob.glob("agent*.py")
        agent_names = [os.path.splitext(file)[0] for file in agent_files]
        agent_names.remove("agent")
        agent_name = random.choice(agent_names)
        print(f"** Agent Refining: {agent_name}")
        return AgentId(agent_name, "default")
    except Exception as e:
        print(f"Exception finding recipient: {e}")
        return AgentId("agent_01", "default")
