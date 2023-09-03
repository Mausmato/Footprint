import streamlit as sl

sl.sidebar.title("Navigation")
sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
sl.title("Hello, welcome to your **DASHBOARD**.")
sl.subheader("Three Main Factors")
col1, col2, col3 = sl.columns(3)

col1.write("this is column1")
col2.write("this is column2")
col3.write("this is column3")