import streamlit as st

def selectBar():
    area = st.selectbox("Select Area", 
        ("All",
         "77th Street", 
         "Central",     
         "Devonshire",  
         "Foothill",   
         "Harbor",     
         "Hollenbeck",
         "Hollywood",   
         "Mission",     
         "N Hollywood", 
         "Newton",      
         "Northeast",   
         "Olympic",    
         "Pacific",     
         "Rampart",     
         "Southeast",   
         "Southwest",   
         "Topanga",     
         "Van Nuys",   
         "West LA",     
         "West Valley", 
         "Wilshire") )
    return area