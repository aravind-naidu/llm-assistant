import streamlit as st
import asyncio
from api.fastapi_client import fetch_bot_response

st.set_page_config(page_title="EV Insight Assistant", page_icon="⚡")
st.title("⚡ EV Insight Assistant")

# Session state for storing chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
if user_input := st.chat_input("Ask me about your EV usage or health..."):
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Fetch bot reply
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

        try:
            response = asyncio.run(fetch_bot_response(user_input))
        except Exception as e:
            response = f"Error: {str(e)}"

        message_placeholder.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
