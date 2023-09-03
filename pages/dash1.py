import streamlit as st

st.sidebar.title("Navigation")
st.sidebar.image("assets/footprint.png")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Hello, welcome to your **DASHBOARD**.")
st.subheader("Three Main Factors")
col1, col2, col3 = st.columns(3)

# Insert HTML content in col1

# Create a link in col3
col1.header("Recommendations")
col1.write("Visit the [Recommendations] Page (http://localhost:8501/Dashboard)")
# Create a link in col2
col2.header("To Do")
col2.write("Visit [ToDo](https://www.google.com)")

# Create a link in col3
col3.header("Strategy")
col3.write("Visit the [Strategy] Page (http://localhost:8501/Strategy)")
