import streamlit as sl
import math
from streamlit_extras.switch_page_button import switch_page
import pickle
with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with open('data.pkl', 'rb') as file:
    total = pickle.load(file)

if sl.button('Previous', on_click = sl.write()):
   switch_page('Shopping & Consumption')

total = round(total/1000, 2)
amt_of_trees = math.ceil(total/0.025)

sl.write("Your total carbon emissions for a year would be "+str(total)+" tons.")  #in tonnes of co2 per year
sl.write('To offset your carbon emissions you would need: '+str(amt_of_trees)+' trees')


if sl.button('CLICK HERE to learn more about how YOU can reduce your carbon footprint', on_click = sl.write()):
   switch_page('Dashboard')


