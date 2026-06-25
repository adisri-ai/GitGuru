"""
chat_message.py
"""

import streamlit as st


def render_chat_message(
    role: str,
    content: str
):

    with st.chat_message(role):

        st.markdown(content)