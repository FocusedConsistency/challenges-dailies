def get_hill_rating(drop, distance, hill_type):
    hill_type_coef = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0
    }
    adj_steepness = drop / distance * hill_type_coef[hill_type]
    if adj_steepness <= 0.1:
        return "Green"
    elif adj_steepness <= 0.25:
        return "Blue"
    else:
        return "Black"

get_hill_rating(95, 900, "Slalom") # should return "Green"
