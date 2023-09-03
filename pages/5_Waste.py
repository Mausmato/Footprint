import streamlit as sl
import math
from streamlit_extras.switch_page_button import switch_page
import pickle
with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

labels = ["Never", "Rarely", "Sometimes", "Often", "Always"]

with open('data.pkl', 'rb') as file:
    total = pickle.load(file)

if sl.button('Previous', on_click = sl.write()):
   switch_page('Diet')
   


q17 = sl.slider('How much waste do you produce a day? ',0, 30,format="%.0flbs") #average is 5 lbs per person

q18 = labels.index(sl.select_slider('How often do you use one-use plastics?', options=labels))

total += 0.315*q17*365+q18*0.03*182.5

with open('data.pkl', 'wb') as file:
    pickle.dump(total, file)

sl.write(total)
  
if sl.button('Next', on_click = sl.write()):
   switch_page('Shopping & Consumption')