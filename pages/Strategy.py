import streamlit as sl

sl.sidebar.image("assets/footprint.png")


with open('style.css') as f:
    sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# sl.title("Hello, welcome to your **DASHBOARD**.")
# sl.subheader("Three Main Factors")

sl.title("Welcome to the **STRATEGY** Tab.")

# Create two columns
left_column, right_column = sl.columns(2)

strategies = {
    "Energy Efficiency": "Learn how to make your home more energy-efficient.",
    "Sustainable Transportation": "Discover eco-friendly transportation options.",
    "Sustainable Diet": "Find tips on reducing your carbon footprint through your diet.",
    "Eco-friendly Travel": "Explore eco-conscious travel practices and destinations.",
    "Carbon Offsetting": "Learn about carbon offsetting and its impact.",
    "Renewable Items": "Try utilizing reuseable items like waterbottles and containters.",
    "Car Tuning": "Keeping your car in tune can help save gas and electricity.",
    "Close the Windows": "When your air conditioner is running, close the windows to save energy.",
    "Composting": "Compost food items to reduce kitchen-waste.",
    "Plant Trees": "Plant trees to help absorb CO2 and produce oxygen.",
    "Smart Home": "Using a smart thermostat can help optimize cooling and heating.",
    "Share Resources": "Borrow and share items with neighbors and friends to reduce consumption.",
    "Appliance Optimizing": "Skip the dryer and air dry clothes to save energy.",
    "Upcycling": "Repair or reuse items to save things from going to waste.",
    "Rain-Barrels": "Utilize rain barrels to catch and store spare water.",
    "Renewable Energy": "Use things like solar power to produce energy."  
}

Selected = left_column.radio("Select a CO2 reduction strategy to review:", list(strategies.keys()))

if Selected:
    right_column.write(" ")
    right_column.write(" ")
    right_column.write(" ")
    right_column.write(" ")
    right_column.write(" ")
    right_column.write(f" **{Selected}**: {strategies[Selected]}") 