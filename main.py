import streamlit as sl

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

sl.markdown("""
‹style>
.css-cio0dv.ea3mdgi1
{
  visibility: hidden;
}
.css-czk5ss.e16jpq800
{
  visibility: hidden
}
</style>
""", unsafe_allow_html=True)

sl.title("FOOTPRINT")
sl.button("Calculate Now")
sl.subheader("Our Mission")
sl.markdown("")

