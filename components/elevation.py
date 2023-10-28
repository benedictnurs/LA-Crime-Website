#Makes the scale 5% of the total data unless it is over 50000 then set automatic value of 2500 to prevent overcrowding
def elevation(data):
    if len(data) < 50000:
        result = (5 / 100) * len(data)
        return result
    else:
        result = 2300
        return result