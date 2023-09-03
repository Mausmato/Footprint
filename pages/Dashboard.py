import streamlit as sl

sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title and header
sl.title("CO2 Emissions Reduction Advisor")
sl.header("Welcome to your personalized guide to lower your annual CO2 emissions!")

# Carbon emissions reduction recommendations
sl.subheader("CO2 Emissions Reduction Recommendations")

# Sidebar for user input
sl.subheader("Please answer a quick question!")
Spend = sl.number_input("How much money are you willing to spend anually to lower your CO2 emissions? (In $)", min_value = 0.0, step=10.0)


if Spend > 0:
    sl.write(f"Your current annual CO2 emissions:")
    sl.write("Here are some recommendations to lower your carbon footprint made for you using the money you are willing to spend:")

#Recommendations for different amount of money they willing to spend
#0-50 dollars
    recommendations1 = [
        "Cheap or even free recommendations, these may seem very small but small steps make a huge difference in the end:"
        "Consider purchasing a bit more second-hand items anually"
        "Tying into that, thrift shop for clothing!"
        "One-use plastics should be limited no matter how much budget you are willing to spend!"
        "Reusuable water bottle is an investment everybody should make"
        "If it's not very hot on summer days, consider opening your windows up instead of unnatural cooling options"
        "Car-pool saves less time and emits less CO2!"
    ]
#50-100 dollars
    recommendations2 = [
        "Here are some more costly recommendations that are also small steps but will result to big things!"
        "Energy-Efficient Light Bulbs are just better economically and have better performance. It's worth the extra price"
        "Plant based meals is an option for anyone to try"
        "If possible, take the bus once or twice a month instead of driving all the time"
        "Home Gardening is worth a try if you have extra time on your hands"
        "Make a rainwater harvest system to conserve a bit of water from your tap"
    ]
#100-200 dollars
    recommendations3 = [
        "Here are some bigger steps you could take!"
        "Be more involved with the community and donating"
        "Eco-Friendly Home Cleaning Products are more expensive but well worth it to emit less CO2"
        "Schedule a professonal energy audit to find ways to strengthen energy efficiency"
        "Public Transportation Passes. Public transport=good"
    ]
#200-500 dollars
    recommendations4 = [
        "Here are some even more costly options that will make a huge difference!"
        "Whilst on vacation, take measures to be more environmentally friendly, such as carbon neutral travel options"
        "Installing LED lights all over your home"
        "Placing indoor plants all around your home improves air quality"
    ]
#500-1000+ dollars
    recommendations5 = [
        "Here are the most expensive options that most people can take. Any of these steps would make a great difference for yourself and the environment."
        "E-bikes are a worth and cool investment"
        "Solar panels are a very great investment to look into"
        "Electric powered lawn tools instead of gas powered"
        "Solar powered electronics are interesting devices to look into"
        "Look into energy efficient home renovations"
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
