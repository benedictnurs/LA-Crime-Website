import datetime as dt
import streamlit as st

def endDate():
    end = st.date_input("Enter end date ", 
                          value = dt.date(2022, 12, 31),
                          min_value=  dt.date(2020, 1, 1),
                          max_value= dt.date(2022,12,31))
    return end