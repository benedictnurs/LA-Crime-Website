import datetime as dt
import streamlit as st

#Function for the date selection
def date(order, year,month,day):
    date = st.date_input(f"Enter {order} date ", 
                          value = dt.date(year, month, day),
                          min_value=  dt.date(2020, 1, 1),
                          max_value= dt.date(2023, 10, 12)
                          )
    return date

