import streamlit as sl
with open('style.css') as f:
  sl.markdown(f'<style>(f.read()</style>', unsafe_allow_html=True)
  
sl.title("Hello, welcome to FOOTPRINT.")

sl.button("Calculate Now")
sl.text("Click here to track your FOOTPRINT")
sl.subheader("Our Mission")
sl.markdown("Here at **FOOTPRINT** we strive to make an eco-friendly environment that is both accessible and practical. ")
