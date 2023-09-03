import streamlit as sl
import math
import pickle
from streamlit_extras.switch_page_button import switch_page

sl.progress(0, text='Completed: 0/5')

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
total = 0

if sl.button('Previous', on_click = sl.write()):
   switch_page('Survey Home')




vehicle_type = [10, 12, 40, 12, 0, 0]
cars= ['Car', 'SUV', 'Semi', 'Pickup', 'Electric', 'None']

q2 = sl.slider('How many kilometres do you travel by car on average in a week', 0, 2000, format = '%.0fkm')

q3 = cars.index(sl.select_slider("What type of vehicle do you use", options = cars))

q4 = sl.slider('How many hours do you fly in an airplane a year?', 0, 100, format = '%.0fhr')

q5 = sl.slider('How many kilometres do you travel using public transportation on average a week?', 0, 1000, format = '%.0fkm')

q6 = sl.slider('How many of your car rides are using a carpool or a ride-sharing app?', 0, 100, format = '%.0f%%')

if q6 > 0:
    total += ((q2/100) * vehicle_type[q3] * 2.3 * 52) / (4 * (q6/100))
else:
    total += ((q2/100) * vehicle_type[q3] * 2.3 * 52) 

total += 9 * q4

total += (q5/100) * 2 * 52

with open('data.pkl', 'wb') as file:
    pickle.dump(total, file)


if sl.button('Next', on_click = sl.write()):
   switch_page('Housing')