import streamlit as sl
from streamlit.components.v1 import html
import pandas as pd
import altair as alt
import numpy as py

sl.set_page_config(page_title='FOOTPRINT')
sl.sidebar.title("Navigation")
sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
sl.title("Hello, welcome to FOOTPRINT.")

import streamlit as st

# Create a title for your app
st.title('To-Do List App')

# Initialize tasks in the session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Create an input field for adding tasks
task = st.text_input('Add a new task:', '')

# Add a button to add tasks to the list
if st.button('Add Task'):
    if task:
        st.session_state.tasks.append({"task": task, "completed": False})
        task = ''

# Display the tasks
st.subheader('Tasks:')
for i, task_info in enumerate(st.session_state.tasks):
    task = task_info["task"]
    completed = task_info["completed"]
    
    # Create a checkbox to mark tasks as completed
    completed = st.checkbox(f"{i + 1}. {task}", completed)
    
    # Update the completed status in the session state
    st.session_state.tasks[i]["completed"] = completed

# Add an option to clear completed tasks
if st.button('Clear Completed Tasks'):
    st.session_state.tasks = [task_info for task_info in st.session_state.tasks if not task_info["completed"]]
