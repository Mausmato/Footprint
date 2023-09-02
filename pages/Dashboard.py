import streamlit as sl
sl.sidebar.title("Navigation")
  
#Feedback API Supposed to show after they finish survey
# app.py

# Title and header
sl.title("CO2 Emissions Reduction Advisor")
sl.header("Welcome to your personalized guide to lower annual CO2 emissions!")

# Sidebar for user input
sl.sidebar.header("User Input")
annual_carbon_emissions = sl.sidebar.number_input("How much money are you willing to spend anually to lower your CO2 emissions? (In $)", min_value = 0.0, step=10.0)

# Carbon emissions reduction recommendations
sl.subheader("CO2 Emissions Reduction Recommendations")

if annual_carbon_emissions > 0:
    sl.write(f"Your current annual CO2 emissions: {annual_carbon_emissions:.2f} metric tons.")
    sl.write("Here are some personalized recommendations to lower your carbon footprint:")

    recommendations = [
        "Reduce energy consumption by improving home insulation and using energy-efficient appliances.",
        "Use public transportation, carpool, or switch to an electric vehicle to reduce transportation emissions.",
        "Reduce meat consumption and incorporate more plant-based foods into your diet.",
        "Limit air travel and choose eco-friendly travel options when possible.",
        "Participate in local environmental initiatives and support renewable energy sources.",
        "Plant trees or participate in reforestation efforts to offset carbon emissions.",
    ]

    sl.write("Here are some personalized recommendations to lower your carbon footprint:")
    for suggestion in recommendations:
        sl.write(f"- {suggestion}")

# Explore carbon reduction strategies
sl.subheader("Explore Carbon Reduction Strategies")

sl.write("Explore more carbon reduction strategies to help you lower your annual CO2 emissions:")

strategies = {
    "1. Energy Efficiency": "Learn how to make your home more energy-efficient.",
    "2. Sustainable Transportation": "Discover eco-friendly transportation options.",
    "3. Sustainable Diet": "Find tips on reducing your carbon footprint through your diet.",
    "4. Eco-friendly Travel": "Explore eco-conscious travel practices and destinations.",
    "5. Carbon Offsetting": "Learn about carbon offsetting and its impact.",
}

selected_strategy = sl.selectbox("Select a carbon reduction strategy:", list(strategies.keys()))

if selected_strategy:
    sl.write(f"**{selected_strategy}**: {strategies[selected_strategy]}")

# Footer
sl.sidebar.markdown("Created for [RhythmHacks]")