#IMPORT MODULES
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import datetime as dt

#IMPORT FUNCTIONS FROM OTHER FILES
from components.coords import *
from components.selectBar import *
from components.date import *
from components.data import *

#Configs the Pages
st.set_page_config(layout="wide", page_title="LA Crime Data")

#Sets the page title 
st.title("Crime Data in LA")


df = data(815882)


#Creates the sidebar for date and select bar
with st.sidebar:
    st.subheader("Filters")
    #Creates the select bar which returns area
    area = selectBar()
    start = str(date("Start", 2020, 1, 1))
    end = str(date("End", 2023, 10, 12))


#Creates a subheader to show which area you selected 
st.subheader(area)


#If area is All then returns 10K rows if not return the specific area only.
if area != "All":
    data_sorted = (df.loc[df['AREA NAME'] == area])
    scale = 5.5
else:
    data_sorted = df.sample(80000)
    scale = 12


#Calls the function from coords.py to use as variables for the map
lat = latitude(area, data_sorted)
lon = longitude(area, data_sorted)


#Filters the data by dates in order to plot within the range also edits the previous variable of data_sorted
data_sorted = data_sorted[(data_sorted['DATE OCC'] > start) & (data_sorted['DATE OCC'] < end)]


#Makes the scale 5% of the total data unless it is over 50000 then set automatic value of 2500 to prevent overcrowding
if len(data_sorted) < 50000:
    result = (5 / 100) * len(data_sorted)
else:
    result = 2300


#Creates the map
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(

        #Lets the lat and lon of the map so it remaps every time you switch area!!!!! Either entire LA or specific selected area
        latitude=lat,
        longitude=lon,

        #Adjusts the zoom important!!!!
        zoom=11,
        pitch=50,
    ),
    layers=[

        #Plots the hexagons important!!!!!
        pdk.Layer(

           'HexagonLayer',

           #Chooses the data that is getting ploted
           data=data_sorted,

           #34.052235 , -118.243683
           #Selects the lon and lats columns in the data 
           get_position='[LON, LAT]',
           radius=200,

           #Scales the hexagons depending on the amount of rows given
           elevation_scale = scale,
           elevation_range=[0, result],
           pickable=True,
           extruded=True,
        )
    ],
))
