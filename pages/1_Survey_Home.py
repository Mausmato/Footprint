import streamlit as sl
import math
from streamlit_extras.switch_page_button import switch_page

if sl.button('Next', on_click = sl.write()):
   switch_page('Transportation')
