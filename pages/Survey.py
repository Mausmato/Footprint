import streamlit as sl
sl.sidebar.title("Navigation")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
labels = ["Never", "Rarely", "Sometimes", "Often", "Always"]
values = [1, 2, 3, 4, 5]


commital = labels.index(sl.select_slider('How committed are you to emit less Carbon Emissions?', options = labels))


q2 = sl.slider('How many kilometres do you drive on average a week', 0, 5000, format = '%.0fkm')

q20 = sl.slider('How much of the products you shop for are second-hand or sustainable products??',0, 100,format="%.0f%")

q21 = labels.index(sl.select_slider('How often do you buy new clothes per year?', options=labels))

q22 = labels.index(sl.select_slider('How often do you buy new electronics per year?', options=labels))

q23 = sl.slider('How many gallons of water do you use daily (in Liters)?',0, 1000,format="%.0fL")


q23_calc = q22/1000*0.25*365