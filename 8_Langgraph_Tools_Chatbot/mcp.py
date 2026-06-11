from unittest import result

from langgraph.graph import StateGraph, START
from dotenv import load_dotenv
from pathlib import Path
import os
import sys
from langchain_core.messages import SystemMessage, HumanMessage

current_dir = os.path.normcase(os.path.normpath(str(Path(__file__).resolve().parent)))
sys.path = [
    path for path in sys.path
    if os.path.normcase(os.path.normpath(str(Path(path or ".").resolve()))) != current_dir
]

from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


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

# MCP client for local FastMCP server
client = MultiServerMCPClient(
    {
        "expenses": {
            "transport": "stdio",
            "command": "c:/projects/langgraph/venv/Scripts/python.exe",
            "args": ["c:/projects/langgraph/8_Langgraph_Tools_Chatbot/mcp_server.py"],
        }
    }
)

# state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

async def build_graph():

    tools = await client.get_tools()

    print(tools)

    llm_with_tools = llm.bind_tools(tools)

    # nodes
    async def chat_node(state: ChatState):

        messages = state["messages"]
        response = await llm_with_tools.ainvoke(messages)
        return {'messages': [response]}

    tool_node = ToolNode(tools)

    # defining graph and nodes
    graph = StateGraph(ChatState)

    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)

    # defining graph connections
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")

    chatbot = graph.compile()

    return chatbot

async def invoke(input_state: ChatState) -> dict:
    chatbot = await build_graph()
    result = await chatbot.ainvoke(input_state)
    return result

async def main():

    chatbot = await build_graph()

    while True:
        user_input = input("Enter your expense question: ")
        result = await invoke({
            "messages": [
                SystemMessage(content="You are a helpful expense assistant."),
                HumanMessage(content=user_input),
            ]
        })
        print(result['messages'][-1].content)

if __name__ == '__main__':
    asyncio.run(main())