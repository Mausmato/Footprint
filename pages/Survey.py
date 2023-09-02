import streamlit as sl

commital = sl.slider('How committed are you to emit less Carbon Emissions?', 0, 100)
min_value2 = 0
max_value2 = 5000
q2 = sl.slider('How many kilometres do you drive on average a week', min_value2, max_value2, format = '%.0fkms')
sl.write(f'Min Value: {min_value2}kms')
sl.write(f'Max Value: {max_value2}kms')

min_value22=0
max_value22=1000
q22 = sl.slider('How many gallons of water do you use daily (in Liters)?',min_value22, max_value22,format="%.0fL")
sl.write(f'Min Value: {min_value22}L')
sl.write(f'Max Value: {max_value22}L')

q22_calc = q22/1000*0.25*365