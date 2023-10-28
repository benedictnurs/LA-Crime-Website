def latitude(area, data_sorted):
    if area == "All":
        areaLat = 34.052235
    else:
        try:
            areaLat = data_sorted["LAT"].iloc[0]
        except:
            return areaLat
    return areaLat

def longitude(area, data_sorted):
    if area == "All":
        areaLon = -118.243683
    else:
        try:
            areaLon = data_sorted["LON"].iloc[0]
        except:
            return areaLon
    return areaLon
