import streamlit as sl

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


sl.title("FOOTPRINT")
sl.button("Calculate Now")
sl.subheader("Our Mission")
sl.markdown("")

