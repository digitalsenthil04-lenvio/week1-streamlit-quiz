import streamlit as st

st.title("🧠 Simple Quiz App")

st.write("Answer the question below:")

question = "What is the capital of India?"
options = ["Mumbai", "Delhi", "Chennai", "Kolkata"]

answer = st.radio(question, options)

if st.button("Submit"):
    if answer == "Delhi":
        st.success("Correct Answer! 🎉")
    else:
        st.error("Wrong Answer ❌ Try again!")
