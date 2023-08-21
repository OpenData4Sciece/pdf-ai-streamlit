import streamlit as st
from streamlit_chat import message

def handle_chat():
    message("How can I help you with as AI assistant?", avatar_style="bottts") # https://www.dicebear.com/styles/bottts

    message("That would be great!", is_user=True,
            avatar_style="adventurer") # https://www.dicebear.com/styles/adventurer

handle_chat()
