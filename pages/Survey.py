import streamlit as sl
sl.sidebar.title("Navigation")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

commital = sl.slider('How committed are you to emit less Carbon Emissions?', 0, 100)

q2 = sl.slider('How many kilometres do you drive on average a week', 0, 5000, format = '%.0fkms')


q22 = sl.slider('How many gallons of water do you use daily (in Liters)?',0, 1000,format="%.0fL")


q22_calc = q22/1000*0.25*365