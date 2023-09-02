import streamlit as sl
sl.sidebar.title("Navigation")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
#Feedback API

import streamlit as st

# Title and header
st.title("Money Saving Advisor")
st.header("Welcome to your personalized money-saving guide!")

# Sidebar for user input
st.sidebar.header("User Input")
money_to_save = st.sidebar.number_input("How much money can you save per month?", min_value=0.01, step=10.0)

# Money-saving suggestions
st.subheader("Money-Saving Suggestions")

if money_to_save > 0:
    st.write(f"You can save ${money_to_save:.2f} per month.")
    st.write("Here are some personalized money-saving suggestions:")

    suggestions = [
        "Create a budget and track your expenses to identify areas where you can cut costs.",
        "Consider automating your savings by setting up automatic transfers to a savings account.",
        "Reduce discretionary spending on non-essential items and focus on needs vs. wants.",
        "Shop for groceries in bulk and take advantage of discounts and coupons.",
        "Explore opportunities to reduce utility bills by improving energy efficiency at home.",
        "Invest in a retirement account like a 401(k) or IRA for long-term savings.",
    ]

    st.write("Here are some personalized money-saving suggestions:")
    for suggestion in suggestions:
        st.write(f"- {suggestion}")

# Financial resources and tips
st.subheader("Financial Resources and Tips")

st.write("Explore more financial resources and tips to help you save money:")

resources = {
    "1. Personal Finance Basics": "Learn the fundamentals of personal finance.",
    "2. Investment Strategies": "Discover different investment options and strategies.",
    "3. Debt Management": "Find ways to manage and reduce your debt effectively.",
    "4. Financial Planning Tools": "Access tools to help you create a financial plan.",
    "5. Savings Calculators": "Calculate your savings goals and timelines.",
}

selected_resource = st.selectbox("Select a financial resource:", list(resources.keys()))

if selected_resource:
    st.write(f"**{selected_resource}**: {resources[selected_resource]}")

# Footer
st.sidebar.markdown("Created by [Your Name]")

  
  