import streamlit as sl
import math
from streamlit_extras.switch_page_button import switch_page
import pickle

sl.sidebar.image("assets/footprint.png")

sl.progress(80, text = 'Completed: 4/5')

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

labels = ["Never", "Rarely", "Sometimes", "Often", "Always"]
labels3 = ['None', 'A few', 'Many', 'Almost all', 'All']

with open('data.pkl', 'rb') as file:
    total = pickle.load(file)

if sl.button('Previous', on_click = sl.write()):
   switch_page('Waste')



q19 = labels3.index(sl.select_slider('How much of the products you shop for are second-hand or sustainable products?', options = labels3))

q20 = labels.index(sl.select_slider('How often do you buy new clothes per year?', options=labels))

q21 = labels.index(sl.select_slider('How often do you buy new electronics per year?', options=labels))

q22 = sl.slider('How many gallons of water do you use daily (in Liters)?',0, 1000,format="%.0fL") # average is 335 liters

values21 = [0,5,10,15,20]
values20 = [0,1,2,4,5]
values19 = [0,5,10,15,20]

total+= 10*values19[q19]+90*values20[q20] + 20*values21[q21] + q22/1000*0.25*365

with open('data.pkl', 'wb') as file:
    pickle.dump(total, file)
    pickle.dump(q19, file)
    pickle.dump(q20, file)
    pickle.dump(q21, file)
    pickle.dump(q22, file)

  
if sl.button('Next', on_click = sl.write()):
   switch_page('Your Results')