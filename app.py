import streamlit as st

st.title("Task Manager Project")

st.write("Welcome to the Task Manager Program.")

name_of_task = st.text_input("Write the name of the task that needs to be performed here:")
date_task_due = st.date_input("The date that the task must be performed by:")
add_task = st.button("Add task to the list of required tasks")
remove_task = st.button("Cick this to remove a task from the task manager")
kill_task_manager = st.button("Click this to end the program")

st.write("Tasks To Do:")

if (add_task == True):
  list_of_tasks += name_of_task, " is due on " , date_task_due, "\n"
st.write(list_of_tasks)
#if (remove_task == True):
