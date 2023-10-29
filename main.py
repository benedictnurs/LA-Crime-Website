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
from components.elevation import *


#Configs the Pages
st.set_page_config(layout="wide", page_title="LA Crime Data")


#Sets the page title 
st.title("Crime Data in Los Angeles")


#Creates dataframe with all the data loaded in
df = data(815882)


#Creates the sidebar for date and select bar
with st.sidebar:
    st.subheader("Filters")
    #Creates the select bar which returns area
    area = selectBar()
    start = str(date("Start", 2020, 1, 1))
    end = str(date("End", 2023, 10, 12))


#Creates a subheader to show which area you selected 


#If area is All then returns 80K rows if not return the specific area only.
data_sorted = data_select(df,area)[0] 
scale = data_select(df,area)[1]


#Caches data for effiecny  filters it through the data selection and returns the data frame

#Data for Hollywood
hollywood_df = data_cache(df, "Hollywood")
data_hollywood = data_select(hollywood_df,"Hollywood")[0]
scale_hollywood = data_select(hollywood_df,"Hollywood")[1]

#Data for Central LA
centeral_df = data_cache(df, "Central")
data_central = data_select(df,"Central")[0]
scale_central = data_select(df,"Central")[1]


#Calls the function from coords.py to use as variables for the map
lat = coords(area, data_sorted,"LAT",34.052235)
lon = coords(area, data_sorted,"LON",-118.243683)

lat_hollywood = coords("Hollywood", data_hollywood,"LAT",34.052235)
lon_hollywood = coords("Hollywood", data_hollywood,"LON",-118.243683)

lat_central = coords("Central", data_central,"LAT",34.052235)
lon_central = coords("Central", data_central,"LON",-118.243683)


#Filters the data by dates in order to plot within the range also edits the previous variable of data_sorted
data_sorted = data_filter_date(data_sorted, start, end)
data_hollywood = data_filter_date(data_hollywood, start, end)
data_central = data_filter_date(data_central, start, end)


#Makes the scale 5% of the total data unless it is over 50000 then set automatic value of 2500 to prevent overcrowding
result = elevation(data_sorted)
result_hollywood = elevation(data_hollywood)
result_central = elevation(data_central)


#Adds columns for multiple maps
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(area)
    map1 = hex_map(lat, lon, data_sorted, scale, result)

with col2:
    st.subheader("Hollywood")
    map2 = hex_map(lat_hollywood, lon_hollywood, data_hollywood, scale_hollywood, result_hollywood)

with col3:
    st.subheader("Central LA")
    map3 = hex_map(lat_central, lon_central, data_central, scale_central, result_central)