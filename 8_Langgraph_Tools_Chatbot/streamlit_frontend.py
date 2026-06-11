import streamlit as st
from langchain_core.messages import HumanMessage

from chatbot import graph


def message_text(content):
	if isinstance(content, str):
		return content
	if isinstance(content, list):
		return "".join(part.get("text", str(part)) if isinstance(part, dict) else str(part) for part in content)
	return str(content)


st.set_page_config(page_title="Tools Chatbot", page_icon="🧮")
st.title("Tools Chatbot")

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	if message.type not in {"human", "ai"} or not message.content:
		continue

	role = "user" if message.type == "human" else "assistant"
	with st.chat_message(role):
		st.markdown(message_text(message.content))

if user_input := st.chat_input("Enter your message"):
	st.session_state.messages.append(HumanMessage(content=user_input))

	with st.chat_message("user"):
		st.markdown(user_input)

	def stream_response():
		final_state = None

		for stream_mode, chunk in graph.stream(
			{"messages": st.session_state.messages},
			stream_mode=["messages", "values"],
		):
			if stream_mode == "messages":
				message_chunk, metadata = chunk
				if metadata.get("langgraph_node") == "chatbot" and message_chunk.content:
					yield message_text(message_chunk.content)
			elif stream_mode == "values":
				final_state = chunk

		if final_state is not None:
			st.session_state.messages = final_state["messages"]

	with st.chat_message("assistant"):
		st.write_stream(stream_response)
