import streamlit as st

st.title("Task Manager Project")

st.write("Welcome to the Task Manager Program.")

name_of_task = st.text_input("Write the name of the task that needs to be performed here:")
date_task_due = st.date_input("The date that the task must be performed by:")
is_clicked = st.button("Add task to the list of required tasks")

st.write("Tasks To Do:")

if (is_clicked == True):
  st.write("Button is Clicked")
