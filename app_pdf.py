import streamlit as st
from streamlit_chat import message
from os import environ as env

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# add sidebar with input field
# allow users to add their own OpenAI API key
user_api_key = st.sidebar.text_input(
    label = "#### OpenAI API Key 🔒",
    placeholder="sk-xxx",
    type="password",
    label_visibility="visible"
)

env["OPENAI_API_KEY"] = user_api_key


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

# if we got the API key, display the file uploader
if user_api_key:
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"]) # allow only PDF file extensions

    # if we receive a CSV file, display the chat conversation
    if uploaded_file is not None:
        # create and load the PDF
        loader = PyPDFLoader(uploaded_file)

        # split and convert PDF pages into text chunks
        pdfPages = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            length_function=len,
            add_start_index=True
        )
        documents = text_splitter.split_documents(pdfPages)

        # display the content of the data
        st.write(documents)


        # show the query input on the chat conversation
        handle_chat()
