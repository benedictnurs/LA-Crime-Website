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


#If area is All then returns 80K random rows if not return the specific area only.
def data_select(df,area):
    if area != "All":
        data_sorted = (df.loc[df['AREA NAME'] == area])
        scale = 5.5
        return data_sorted , scale
    else:
        data_sorted = df.sample(80000)
        scale = 12
        return data_sorted , scale
    
    
#Filters the data by dates in order to plot within the range also edits the previous variable of data_sorted
def data_filter_date(data_sorted, start, end):
    data = data_sorted[(data_sorted['DATE OCC'] > start) & (data_sorted['DATE OCC'] < end)]
    return data

#Caches constant dataframes to reduce runtime
@st.cache_data
def data_cache(df,location):
    data_frame = data_select(df, location)[0]
    return data_frame