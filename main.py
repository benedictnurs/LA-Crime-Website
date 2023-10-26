import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide", page_title="LA Crime Data")

@st.cache_resource
def data():
    crime_data = pd.read_csv("Crime.csv")
    return crime_data
data = data()

print(data.head())

st.title("Crime Data in LA")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=34.0549,
        longitude=-118.2426,
        zoom=8.5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))