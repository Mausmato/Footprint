import streamlit as sl
from Survey import *

sl.sidebar.title("Navigation")
sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title and header
sl.title("CO2 Emissions Reduction Advisor")
sl.header("Welcome to your personalized guide to lower annual CO2 emissions!")

# Carbon emissions reduction recommendations
sl.subheader("CO2 Emissions Reduction Recommendations")

# Sidebar for user input
sl.subheader("User Input")
Spend = sl.number_input("How much money are you willing to spend anually to lower your CO2 emissions? (In $)", min_value = 0.0, step=10.0)


if Spend > 0:
    sl.write(f"Your current annual CO2 emissions:")
    sl.write("Here are some recommendations to lower your carbon footprint made for you using the money you are willing to spend:")

#Recommendations for different amount of money they willing to spend
    recommendations1 = [
        "Reduce energy consumption by improving home insulation and using energy-efficient appliances.",
        "Use public transportation, carpool, or switch to an electric vehicle to reduce transportation emissions.",
        "Reduce meat consumption and incorporate more plant-based foods into your diet.",
        "Limit air travel and choose eco-friendly travel options when possible.",
        "Participate in local environmental initiatives and support renewable energy sources.",
        "Plant trees or participate in reforestation efforts to offset carbon emissions.",
    ]
    recommendations2 = [
        
    ]
    recommendations3 = [
        
    ]
    recommendations4 = [
        
    ]
    recommendations5 = [
        
    ]

    sl.write("Personalized recommendations:")
    for suggestion in recommendations1:
        sl.write(f"- {suggestion}")

# Explore carbon reduction strategies
sl.subheader("Explore Carbon Reduction Strategies")

sl.write("Explore more carbon reduction strategies to help you lower your annual CO2 emissions:")

#Strategies for from results of the survey such as alot of red meat, not sustainable energy, etc. Show like 5 from this list relevant to user result.
strategies = {
    "1. Energy Efficiency": "Learn how to make your home more energy-efficient.",
    "2. Sustainable Transportation": "Discover eco-friendly transportation options.",
    "3. Sustainable Diet": "Find tips on reducing your carbon footprint through your diet.",
    "4. Eco-friendly Travel": "Explore eco-conscious travel practices and destinations.",
    "5. Carbon Offsetting": "Learn about carbon offsetting and its impact.",
}

selected_strategy = sl.selectbox("Select a carbon reduction strategy to learn more about!:", list(strategies.keys()))

if selected_strategy:
    sl.write(f"**{selected_strategy}**: {strategies[selected_strategy]}")

# Footer
sl.sidebar.markdown("Created for [RhythmHacks]")