import streamlit as st
import pydeck as pdk

#Plots the coords needed to map
def coords(area, data_sorted, position, default):
    if area == "All":
        areaLat = default
    else:
        try:
            areaLat = data_sorted[position].iloc[0]
        except:
            return areaLat
    return areaLat


#Creates the map
def hex_map(lat, lon, data_sorted, scale, result):
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

           #Selects the lon and lats columns in the data 
           get_position='[LON, LAT]',
           radius=200,

           #Scales the hexagons depending on the amount of rows given
           elevation_scale = scale,

           #Elevation of the hexagons
           elevation_range=[0, result],
           pickable=True,
           extruded=True,
        )
    ],
))