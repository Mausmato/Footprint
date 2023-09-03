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