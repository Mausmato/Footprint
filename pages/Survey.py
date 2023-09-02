import streamlit as sl
import math

sl.sidebar.title("Navigation")
sl.sidebar.image("assets/footprint.png")

sl.title("Welcome to the Survey.")
sl.subheader("This is our curated survey to help you keep track of your carbon footprint.")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

labels = ["Never", "Rarely", "Sometimes", "Often", "Always"]
labels2 = ['Never', 'Rarely', 'Sometimes', 'Often', 'Very often']
labels3 = ['None', 'A few', 'Many', 'Almost all', 'All']
values = [1, 2, 3, 4, 5]
vehicle_type = [10, 12, 40, 12, 0]
car_type = ['car', 'SUV', 'semi', 'pickup', 'electric']

commital = sl.slider('How committed are you to emit less Carbon Emissions? (on a scale of 1-10)', 1, 10)

total = 0




#transportation
q2 = sl.slider('How many kilometres do you drive on average a week', 0, 5000, format = '%.0fkm')

q3 = car_type.index(sl.selectbox('What type of vehicle do you drive', car_type))

q4 = sl.slider('How many hours do you fly in an airplane a year?', 0, 100, format = '%.0fhr')

q5 = sl.slider('How many kilometres do you drive using public transportation on average a week?', 0, 1000, format = '%.0fkm')

q6 = sl.slider('How many of your car rides are using a carpool or a ride-sharing app?', 0, 100, format = '%.0f%%')

if q6 > 0:
    total += ((q2/100) * vehicle_type[q3] * 2.3 * 52) / (4 * (q6/100))
else:
    total += ((q2/100) * vehicle_type[q3] * 2.3 * 52) 

total += 9 * q4

total += (q5/100) * 2 * 52

#housing
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

#diet
q12 = sl.selectbox('What sort of diet do you follow', ['None', 'vegan', 'vegetarian'])

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


#waste
q17 = sl.slider('How much waste do you produce a day? ',0, 30,format="%.0flbs") #average is 5 lbs per person

q18 = labels.index(sl.select_slider('How often do you use one-use plastics?', options=labels))

total += 0.315*q17*365+q18*0.03*182.5

#shopping and consumption
q19 = labels3.index(sl.select_slider('How much of the products you shop for are second-hand or sustainable products?', options = labels3))

q20 = labels.index(sl.select_slider('How often do you buy new clothes per year?', options=labels))

q21 = labels.index(sl.select_slider('How often do you buy new electronics per year?', options=labels))

#water usage
q22 = sl.slider('How many gallons of water do you use daily (in Liters)?',0, 1000,format="%.0fL") # average is 335 liters

commital = sl.slider('Now that you are more educated, how committed are you to emit less Carbon Emissions? (on a scale of 1-10)', 1, 10)

values21 = [0,5,10,15,20]
values20 = [0,1,2,4,5]
values19 = [0,5,10,15,20]


#q19, 20,21,22 
total+= 10*values19[q19]+90*values20[q20] + 20*values21[q21] + q22/1000*0.25*365

total = round(total/1000, 2)
sl.write("Your total carbon emissions for a year would be "+str(total)+" tons.")  #in tonnes of co2 per year
amt_of_trees = math.roof(total/0.025)
sl.write('To offset your carbon emissions you would need:'+str(amt_of_trees)+'trees')