import streamlit as sl
import math
from streamlit_extras.switch_page_button import switch_page
import pickle

sl.sidebar.image("assets/footprint.png")

sl.progress(20, text='Completed: 1/5')

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

labels2 = ['Never', 'Rarely', 'Sometimes', 'Often', 'Very often']
labels3 = ['None', 'A few', 'Many', 'Almost all', 'All']

with open('data.pkl', 'rb') as file:
    total = pickle.load(file)

if sl.button('Previous', on_click = sl.write()):
   switch_page('Transportation')
   


q7 = sl.slider('What is the square footage of your home', 0, 10000, format = '%.0fsq')

q8 = sl.radio('Do you use electric or gas heating and cooling systems:', ['gas', 'electric', 'I do not know'])

q9 = labels2.index(sl.select_slider('How often do you adjust your thermostat settings', options = labels2))

q10 = sl.radio('Have you implemented any renewable energy sources at home (e.g., solar panels)?', ['yes', 'no'])

q11 = labels3.index(sl.select_slider('How many appliances/utilities do you own that are energy efficient (blue energy star sticker)?', options = labels3))

if q8 == 'electric':
 total += (2.47 * q7 * 0.3712) * q9/2
elif q8 == 'gas':
  total += (0.954 * q7 * 1.9) * q9/2
elif q8 == 'I do not know':
  total += ((2.47 * q7 * 0.3712 + 0.954 * q7 * 1.9)/2) * q9/2

total += q11 * 100 + 500

if q10 == 'yes':
   total -= 557

with open('data.pkl', 'wb') as file:
    pickle.dump(total, file)
    pickle.dump(q7, file)
    pickle.dump(q8, file)
    pickle.dump(q9, file)
    pickle.dump(q10, file)
    pickle.dump(q11, file)

   
if sl.button('Next', on_click = sl.write()):
   switch_page('Diet')
