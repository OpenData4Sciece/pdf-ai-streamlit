import streamlit as st

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
        

