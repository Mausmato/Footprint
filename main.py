import streamlit as sl


sl.markdown("""
‹style>
.css-1wbqy5l e17vllj40 {
  visibility: hidden;
  
  
}

.css-cio0dv ea3mdgi1 {
  
  visibility: hidden
  
}
</style>
""", unsafe_allow_html=True)

sl.title("Hello, welcome to FOOTPRINT.")

sl.button("Calculate Now")
sl.text("Click here to track your FOOTPRINT")
sl.subheader("Our Mission")
sl.markdown("Here at **FOOTPRINT** we strive to make an eco-friendly environment that is both accessible and practical. ")
with open('style.css') as f:
  sl.markdown(f'<style>(f.read()</style>', unsafe_allow_html=True)