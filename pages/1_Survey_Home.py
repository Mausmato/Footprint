import streamlit as sl
import math
from streamlit_extras.switch_page_button import switch_page

sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

sl.title('CARBON FOOTPRINT Calculator')
sl.subheader('5 minute quiz')

if sl.button('Next', on_click = sl.write()):
   switch_page('Transportation')

