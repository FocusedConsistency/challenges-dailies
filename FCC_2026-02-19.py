def avalanche_risk(snow_depth, slope):
    if snow_depth == "Shallow" or slope == "Gentle":
        return "Safe"
    return "Risky"
