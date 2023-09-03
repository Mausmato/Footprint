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
# Create a title for your app
sl.title('To-Do List App')

# Initialize tasks in the session state
if 'tasks' not in sl.session_state:
    sl.session_state.tasks = []

# Create an input field for adding tasks
task = sl.text_input('Add a new task:', '')

# Add a button to add tasks to the list
if sl.button('Add Task'):
    if task:
        sl.session_state.tasks.append({"task": task, "completed": False})
        task = ''

# Display the tasks
sl.subheader('Tasks:')
for i, task_info in enumerate(sl.session_state.tasks):
    task = task_info["task"]
    completed = task_info["completed"]
    
    # Create a checkbox to mark tasks as completed
    completed = sl.checkbox(f"{i + 1}. {task}", completed)
    
    # Update the completed status in the session state
    sl.session_state.tasks[i]["completed"] = completed

# Add an option to clear completed tasks
if sl.button('Clear Completed Tasks'):
    sl.session_state.tasks = [task_info for task_info in sl.session_state.tasks if not task_info["completed"]]
