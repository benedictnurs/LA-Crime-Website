#Plots the coords needed to map
def latitude(area, data_sorted, position, default):
    if area == "All":
        areaLat = default
    else:
        try:
            areaLat = data_sorted[position].iloc[0]
        except:
            return areaLat
    return areaLat




