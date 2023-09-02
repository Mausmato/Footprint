import streamlit as sl
sl.sidebar.title("Navigation")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
labels = ["Never", "Rarely", "Sometimes", "Often", "Always"]
values = [1, 2, 3, 4, 5]


commital = labels.index(sl.select_slider('1. How committed are you to emit less Carbon Emissions?', options = labels))


q2 = sl.slider('2. How many kilometres do you drive on average a week', 0, 5000, format = '%.0fkm')

q3 = sl.selectbox('3. What type of vehicle do you drive', ['car', 'SUV', 'electric', 'semi', 'pickup'])

q13 = sl.selectbox('3. What type of vehicle do you drive', ['None', 'vegan', 'vegetarian'])

q14 = labels.index(sl.select_slider('How often do you eat red meat? (Beef, Pork, Lamb, etc)', options=labels))

q15 = labels.index(sl.select_slider('How often do you eat white meat? (Fish,Chicken,Turkey)', options=labels))

q16 = labels.index(sl.select_slider('16. How often do you eat dairy products?', options=labels))

q17 = sl.slider('17. How much of the food you buy is locally produced',0, 100,format="%.0f%%")

q18 = sl.slider('18. How much waste do you produce a day? ',0, 30,format="%.0flbs") #average is 5 lbs per person

q19 = labels.index(sl.select_slider('19. How often do you use one-use plastics?', options=labels))

q20 = sl.slider('20. How much of the products you shop for are second-hand or sustainable products?',0, 100,format="%.0f%%")

q21 = labels.index(sl.select_slider('21. How often do you buy new clothes per year?', options=labels))

q22 = labels.index(sl.select_slider('22. How often do you buy new electronics per year?', options=labels))

q23 = sl.slider('23. How many gallons of water do you use daily (in Liters)?',0, 1000,format="%.0fL") # average is 335 liters


q22_calc = q22/1000*0.25*365