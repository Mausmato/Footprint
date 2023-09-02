import streamlit as sl
sl.sidebar.title("Navigation")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
labels = ["Never", "Rarely", "Sometimes", "Often", "Always"]
labels2 = ['Never', 'Rarely', 'Sometimes', 'Often', 'Very often']
values = [1, 2, 3, 4, 5]
vehicle_type = [10, 12, 40, 12, 0]
car_type = ['car', 'SUV', 'semi', 'pickup', 'electric']


commital = labels.index(sl.select_slider('How committed are you to emit less Carbon Emissions?', options = labels))

total = 0

#transportation
q2 = sl.slider('How many kilometres do you drive on average a week', 0, 5000, format = '%.0fkm')

q3 = car_type.index(sl.selectbox('What type of vehicle do you drive', car_type))

q4 = sl.slider('How many hours do you fly in an airplane?', 0, 100, format = '%.0fhr')

q5 = sl.slider('How many kilometres do you drive using public transportation on average a week?', 0, 1000, format = '%.0fkm')

q6 = sl.slider('How many of your car rides are using a carpool or a ride-sharing app?', 0, 100, format = '%.0f%%')

total += ((q2/100) * vehicle_type[q3] * 2.3 * 52) / (4 * (q6/100))

total += #for airplane calculate the co2 emmissions and then divide by amount of people in a plane

total += #for public tranport calculate the emmissions and divide by amnt of people on the bus

#housing
q7 = sl.slider('What is the square footage of your home', 0, 10000, format = '%.0fsq')

q8 = sl.radio('Do you use electric or gas heating and cooling systems:', ['gas', 'electric'])

q9 = labels2.index(sl.select_slider('How often do you adjust your thermostat settings', options = labels2))

q10 = sl.radio('Have you implemented any renewable energy sources at home (e.g., solar panels)?', ['yes', 'no'])

q11 = sl.select_slider('How many appliances/utilities do you own that are energy efficient (blue energy star sticker)?', options = ['None', 'A few', 'Many', 'Almost all', 'All'])

#diet
q12 = sl.selectbox('What sort of diet do you follow', ['None', 'vegan', 'vegetarian'])

q13 = labels.index(sl.select_slider('How often do you eat red meat? (Beef, Pork, Lamb, etc)', options=labels))

q14 = labels.index(sl.select_slider('How often do you eat white meat? (Fish,Chicken,Turkey)', options=labels))

q15 = labels.index(sl.select_slider('How often do you eat dairy products?', options=labels))

q16 = sl.slider('How much of the food you buy is locally produced',0, 100,format="%.0f%%")

#waste
q17 = sl.slider('How much waste do you produce a day? ',0, 30,format="%.0flbs") #average is 5 lbs per person

q18 = labels.index(sl.select_slider('How often do you use one-use plastics?', options=labels))

#shopping and consumption
q19 = sl.slider('How much of the products you shop for are second-hand or sustainable products?',0, 100,format="%.0f%%")

q20 = labels.index(sl.select_slider('How often do you buy new clothes per year?', options=labels))

q21 = labels.index(sl.select_slider('How often do you buy new electronics per year?', options=labels))

#water usage
q22 = sl.slider('How many gallons of water do you use daily (in Liters)?',0, 1000,format="%.0fL") # average is 335 liters

commital = labels.index(sl.select_slider('Now that you are more educated, how committed are you to emit less Carbon Emissions?', options = labels))

values1 = [0,5,10,15,20]
values2 = [0,1,2,4,5]


#q20,21,22 
total+= 90*values2[q20] + 20*values1[q21] + q22/1000*0.25*365