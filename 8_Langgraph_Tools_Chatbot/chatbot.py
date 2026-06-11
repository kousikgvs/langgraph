from pathlib import Path
from typing import Annotated, TypedDict

from langchain_groq import ChatGroq
from langchain_core.messages import AnyMessage, HumanMessage
from langchain_core.tools import tool
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

env_path = Path.cwd() / ".env"
if not env_path.exists():
    env_path = Path.cwd().parent / ".env"
load_dotenv(env_path)  # Load environment variables from workspace root .env file

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b


tools = [add, multiply]
llm_with_tools = llm.bind_tools(tools)


def generate(state: State) -> dict:
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(State)

builder.add_node("chatbot", generate)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")

graph = builder.compile()


if __name__ == "__main__":
    input_state = {"messages": []}

    while True:
        input_user = input("Enter your message: ")
        # input_state["messages"].append(HumanMessage(content=input_user))

        for stream_mode, chunk in graph.stream(input_state, stream_mode=["messages", "values"]):
            if stream_mode == "messages":
                message_chunk, _ = chunk
                if message_chunk.content:
                    print(message_chunk.content, end="", flush=True)
            elif stream_mode == "values":
                input_state["messages"] = chunk["messages"]

        print()