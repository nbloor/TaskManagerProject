import streamlit as st

st.title("Task Manager Project")

st.write("Welcome to the Task Manager Program.")


name_of_task = st.text_input("Write the name of the task that needs to be performed here:")
date_task_due = st.date_input("The date that the task must be performed by:")
st.button("Click me")
