import streamlit as sl
import math
from streamlit_extras.switch_page_button import switch_page
import pickle

sl.progress(40, text = 'Completed: 2/5')

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

labels = ["Never", "Rarely", "Sometimes", "Often", "Always"]

with open('data.pkl', 'rb') as file:
    total = pickle.load(file)

if sl.button('Previous', on_click = sl.write()):
   switch_page('Housing')

q12 = sl.radio('What sort of diet do you follow', ['None', 'vegan', 'vegetarian'])

if q12 == "None":
    
    q13 = labels.index(sl.select_slider('How often do you eat red meat? (Beef, Pork, Lamb, etc)', options=labels))

    q14 = labels.index(sl.select_slider('How often do you eat white meat? (Fish,Chicken,Turkey)', options=labels))

    q15 = labels.index(sl.select_slider('How often do you eat dairy products?', options=labels))
    
    q16 = sl.slider('How much of the food you buy is locally produced',0, 100,format="%.0f%%")

    total += 550*q13/2+354*q14/2+208*q15/2+q16*0.118*q16/300+(100-q16)*11.8*(100-q16)/300

elif q12 == 'vegetarian':

    q15 = labels.index(sl.select_slider('How often do you eat dairy products?', options=labels))
    q16 = sl.slider('How much of the food you buy is locally produced',0, 100,format="%.0f%%")

    total += 208*q15/2+q16*0.118*q16/300+(100-q16)*11.8*(100-q16)/300

else:

    q16 = sl.slider('How much of the food you buy is locally produced',0, 100,format="%.0f%%")

    total += q16*0.118*q16/300+(100-q16)*11.8*(300-q16)/300

with open('data.pkl', 'wb') as file:
    pickle.dump(total, file)

if sl.button('Next', on_click = sl.write()):
   switch_page('Waste')