from typing import Annotated
from pydantic import BaseModel
from langgraph.graph import StateGraph
from langgraph.graph import START, END

# Reducer: retain the last updated value
def last_value(_, new):
    return new

# Step 1: Define the state schema
class MyState(BaseModel):
    count: Annotated[int, last_value]

# Step 2: Initialize the graph
builder = StateGraph(MyState)

# Step 3: Define nodes
def increment_node(state: MyState) -> dict:
    new_count = state.count + 1
    print(f"🟢 Incremented count to {new_count}")
    return {"count": new_count}

def stop_node(state: MyState) -> dict:
    print(f"🛑 Stopping at count = {state.count}")
    return {"count": state.count}

# Register nodes
builder.add_node("increment", increment_node)
builder.add_node("stop", stop_node)

# Step 4: Define graph edges
def decide_next(state: MyState) -> str:
    return "stop" if state.count >= 3 else "increment"

# Use START and END
builder.add_edge(START, "increment")
builder.add_conditional_edges("increment", decide_next, ["increment", "stop"])
builder.add_edge("stop", END)

# Step 5: Compile and run
app = builder.compile()

# One `invoke()` call = one **super-step**
print("\n🔁 First super-step:")
state = app.invoke({"count": 0})

print("\n🔁 Second super-step:")
state = app.invoke(state)

print("\n🔁 Third super-step:")
state = app.invoke(state)

print("\n🔁 Fourth super-step:")
state = app.invoke(state)

print("\n✅ Final State:", state)
