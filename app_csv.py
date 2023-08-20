from os import environ as env

import streamlit as st
import pandas as pd

from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI

env["OPENAI_API_KEY"] = "sk-xxx" # Replace with your API key


st.title(":sunglasses: Analysis Assistant :sunglasses:")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv ")

# If we receive a CSV file
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe)

    question = st.text_input("What's your question?")
    button = st.button("Ask :robot_face:")

    if button:
        st.success("You asked: " + question, icon="🤖")
