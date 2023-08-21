import streamlit as st
from streamlit_chat import message

def handle_chat():
    # initialize session state for user and bot messages
    if "user" not in st.session_state:
        st.session_state["user"] = []
    if "bot" not in st.session_state:
        st.session_state["bot"] = []

    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input(
            "Question:",
            placeholder="Ask queries related to the PDF content",  
            key="user_input"
        )
        submit_button = st.form_submit_button(label="Query")

    # if we receive a user input and the submit button was pressed
    if submit_button and user_input:
        answer = "Echo: " + user_input
        # store user and bot messages to session state
        st.session_state["user"].append(user_input)
        st.session_state["bot"].append(answer)

    if st.session_state["bot"]:
        for saved_message in range(len(st.session_state["bot"]) -1, -1, -1): # iterate backwards with reversed range -1
            message(
                st.session_state["bot"][saved_message],
                key=str(saved_message),
                avatar_style="bottts") # https://www.dicebear.com/styles/bottts

            message(
                st.session_state["user"][saved_message],
                key=str(saved_message) + "user_",
                is_user=True,
                avatar_style="adventurer") # https://www.dicebear.com/styles/adventurer

handle_chat()
