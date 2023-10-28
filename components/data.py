import streamlit as st
import pandas as pd

#Caches the data so we don't have to keep loading it.
#Gets the first 40K rows for now.
@st.cache_resource
def data(rows):
    crime_data = pd.read_csv("Crime.csv",
                             nrows=rows, 
                             usecols= ["AREA NAME", "LAT", "LON","DATE OCC"],
                             parse_dates=["DATE OCC"]   
  )
    return crime_data