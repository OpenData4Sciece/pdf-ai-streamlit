###
# Author: Pierre-Henry Soria <hi@ph7.me>

# This is a Streamlit app that uses a CSV file as a knowledge base.
# It uses the OpenAI API to answer questions.
# It is a simple example of how to use the LangChain library.
# To run it, type in your terminal:
# streamlit run app_csv.py
###

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

    llm = OpenAI(temperature=0) # Create the OpenAI language model
    agent = create_pandas_dataframe_agent(llm, dataframe, verbose=True)

    if button: # If the user clicks the button
        answer = agent.run(question) # Run the agent
        st.success(answer, icon="🤖")
