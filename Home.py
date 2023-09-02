import streamlit as sl
from streamlit.components.v1 import html

sl.sidebar.title("Navigation")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
sl.title("Hello, welcome to FOOTPRINT.")
sl.button('Calculate Now')
sl.markdown("Click here to track your **FOOTPRINT** with our curated survey.")
sl.subheader("Our Mission")
sl.markdown("  Here at **FOOTPRINT** we strive to make an eco-friendly environment that is both accessible and practical. We have created a platform where users can track and calculate their **carbon footprints** to see exactly how much of an impact they have on our lovley planet. After all, a little goes a long way.")

