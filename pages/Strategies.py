import streamlit as sl

sl.sidebar.image("assets/footprint.png")


with open('style.css') as f:
    sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# sl.title("Hello, welcome to your **DASHBOARD**.")
# sl.subheader("Three Main Factors")

sl.title("Welcome to the **STRATEGIES** Tab.")

# Create two columns
left_column, right_column = sl.columns(2)

strategies = {
    "Energy Efficiency": "Use more energy efficient appliances, such as making the switch from incandescent bulbs to LEDs.",
    "Sustainable Transportation": "Using public transport such as trains and buses. Cycling more to get to nearby destinations and investing in green vehicles.",
    "Sustainable Diet": "Buying more locally foods help reduce emissions as non-locally sourced foods emit 100x more.",
    "Carbon Offsetting": "Planting trees is one of may ways to reach carbon neutrality and balancing out the emissions you produce.",
    "Renewable Items": "Using renewable items such as multi-use waterbottles and purchasing items second-hand when possible.",
    "Close the Windows": "When your air conditioner is running, close the windows to conserve energy.",
    "Composting": "Compost food items to reduce kitchen-waste.",
    "Plant Trees": "Plant trees to help absorb more CO2 and produce more oxygen.",
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