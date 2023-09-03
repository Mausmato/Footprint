import streamlit as sl
from streamlit.components.v1 import html
import pandas as pd
import altair as alt
import numpy as py
from streamlit_extras.switch_page_button import switch_page

sl.set_page_config(page_title='FOOTPRINT')
sl.sidebar.image("assets/footprint.png")
sl.sidebar.image("assets/vine.png")

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
    

if sl.button('**CALCULATE NOW**', on_click = sl.write()):
   switch_page('Survey Home')
# sl.markdown('<a href="/Survey" target="_self">**CALCULATE NOW**</a>', unsafe_allow_html=True)
sl.markdown("Click here to track your **FOOTPRINT** with our curated survey.")
sl.subheader("Our Mission")
sl.markdown("  Here at **FOOTPRINT** we strive to make an eco-friendly environment that is both accessible and practical. We have created a platform where users can track and calculate their **carbon footprints** to see exactly how much of an impact they have on our lovley planet. After all, a little goes a long way.")

sl.subheader("The Facts")
wwdata = {"DATES":[2012, 2013, 2014, 2015, 2016 ,2017, 2018, 2019, 2020, 2021], "EMISSIONS IN BILLION METRIC TONNES":[37.12, 35.26, 37.08, 36.83, 36.1, 35.52, 35.56, 35.58, 35.32, 35.01]}

wwdata=pd.DataFrame(wwdata)

wwdata = wwdata.set_index("DATES")

wwwdata = {"DATESS":[2012, 2013, 2014, 2015, 2016 ,2017, 2018, 2019, 2020, 2021], "EMISSIONS IN MILLION METRIC TONNES":[545.6,534.9,584.7,584.4,571.5,560.5,574.3,569.8,572.6,568.2]}

wwwdata=pd.DataFrame(wwwdata)

wwwdata = wwwdata.set_index("DATESS")
sl.write("Yearly Carbon Emissions for the World and for Canada from 2012-2021.")
sl.line_chart(wwdata)
sl.caption("A chart of CO2 emissions in billions of metric tonnes worldwide.")
sl.line_chart(wwwdata)
sl.caption("A chart of CO2 emissions in millions of metric tonnes in Canada.")

sl.write("Comparison between an average person in Canada and in the World's annual emissions in 2022.")
g1data = {"Location":["Canada","World"],"Average annual Emmisions per Person":[14.86,4.7]}
g1data = pd.DataFrame(g1data)
g1data = g1data.set_index("Location")
sl.bar_chart(g1data)

sl.write("The Best and Worst Environmental Performance Index (EPI) and where Canada stands.")
g3data = {"Location":["Denmark","UK","Finland","Malta","Sweden","Canada","Pakistan","Bangladesh","Vietnam","Myanmar","India"],"EPI Rating":[77.9,77.7,76.5,75.2,72.7,50,24.6,23.1,20.1,19.4,18.9]}
g3data = pd.DataFrame(g3data)
g3data = g3data.set_index("Location")
sl.altair_chart(g3data)
sl.subheader("SUMMARY")
sl.write("Much like other **first-world countries**, Canada is **on par** with a majority of the world when it comes to **green** action. Canada is not too far above average, but far from below it. It seems that Canada generally follows the trends that the rest of world does and though Canada comes just **50th in the world** when it comes to their **Environmental Performance Index (EPI)**, their yearly carbon emissions for the average person living in Canada is **on the decline.**")