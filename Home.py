import streamlit as sl
from streamlit.components.v1 import html
import pandas as pd
import numpy as py
sl.set_page_config(page_title='FOOTPRINT')
sl.sidebar.title("Navigation")
sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
  sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
sl.title("Hello, welcome to FOOTPRINT.")
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
    

sl.markdown('<a href="/Survey" target="_self">CALCULATE NOW</a>', unsafe_allow_html=True)
sl.button('**CALCULATE NOW**', on_click=open_page, args=('http://localhost:8502/Survey',))
sl.markdown("Click here to track your **FOOTPRINT** with our curated survey.")
sl.subheader("Our Mission")
sl.markdown("  Here at **FOOTPRINT** we strive to make an eco-friendly environment that is both accessible and practical. We have created a platform where users can track and calculate their **carbon footprints** to see exactly how much of an impact they have on our lovley planet. After all, a little goes a long way.")

sl.subheader("The Facts")
wwdata = {"DATES":[2012, 2013, 2014, 2015, 2016 ,2017, 2018, 2019, 2020, 2021], "EMMISIONS IN BILLION METRIC TONNES":[37.12, 35.26, 37.08, 36.83, 36.1, 35.52, 35.56, 35.58, 35.32, 35.01]}

wwdata=pd.DataFrame(wwdata)

wwdata = wwdata.set_index("DATES")

wwwdata = {"DATESS":[2012, 2013, 2014, 2015, 2016 ,2017, 2018, 2019, 2020, 2021], "EMMISIONS IN MILLION METRIC TONNES":[545.6,534.9,584.7,584.4,571.5,560.5,574.3,569.8,572.6,568.2]}

wwwdata=pd.DataFrame(wwwdata)

wwwdata = wwwdata.set_index("DATESS")

sl.line_chart(wwdata)
sl.write("A chart of CO2 emissions in billions of metric tonnes from 2012-2021 worldwide.")
sl.line_chart(wwwdata)
sl.write("A chart of CO2 emissions in millions of metric tonnes from 2012-2021 in Canada.")


sl.subheader("Summary")