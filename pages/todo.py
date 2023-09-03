import streamlit as sl
from streamlit.components.v1 import html
import altair as alt
import numpy as py
import pandas as pd
from datetime import datetime

sl.set_page_config(page_title='FOOTPRINT')
sl.sidebar.title("Navigation")
sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
sl.title("Hello, welcome to FOOTPRINT.")

# Create a title for your app
sl.title('Advanced To-Do List App')

# Initialize tasks in the session state
if 'tasks' not in sl.session_state:
    sl.session_state.tasks = pd.DataFrame(columns=['Task', 'Priority', 'Due Date'])

# Create input fields for adding tasks
task = sl.text_input('Add a new task:', '')
priority = sl.selectbox('Priority:', ['Low', 'Medium', 'High'])
due_date = sl.date_input('Due Date:', datetime.today())

# Add a button to add tasks to the list
if sl.button('Add Task'):
    if task:
        new_task = {'Task': task, 'Priority': priority, 'Due Date': due_date}
        sl.session_state.tasks = pd.concat([sl.session_state.tasks, pd.DataFrame([new_task])], ignore_index=True)
        task = ''
        priority = 'Low'
        due_date = datetime.today()

# Create task filtering options
sl.sidebar.header('Task Filters')
selected_priority = sl.sidebar.selectbox('Select Priority:', ['All', 'Low', 'Medium', 'High'])
show_completed = sl.sidebar.checkbox('Show Completed Tasks')

# Filter and display tasks
filtered_tasks = sl.session_state.tasks.copy()

if selected_priority != 'All':
    filtered_tasks = filtered_tasks[filtered_tasks['Priority'] == selected_priority]

if not show_completed:
    filtered_tasks = filtered_tasks[~filtered_tasks['Task'].str.startswith('[Completed]')]

sl.subheader('Tasks:')
for i, row in filtered_tasks.iterrows():
    task = row['Task']
    priority = row['Priority']
    due_date = row['Due Date'].strftime('%Y-%m-%d')
    task_label = f"{i + 1}. {task} (Priority: {priority}, Due Date: {due_date})"
    completed = sl.checkbox(task_label, False)
    
    # Update the task status in the session state
    if completed:
        sl.session_state.tasks.loc[i, 'Task'] = f"[Completed] {task}"

# Add an option to clear completed tasks
if sl.button('Clear Completed Tasks'):
    sl.session_state.tasks = filtered_tasks[~filtered_tasks['Task'].str.startswith('[Completed]')]
