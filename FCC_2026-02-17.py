def check_eligibility(athlete_weights, sled_weight):
    min_sled_weights = {
        1: 165,
        2: 170,
        4: 210
    }
    max_weights = {
        1: 247,
        2: 390,
        4: 630
    }
    athlete_count = len(athlete_weights)
    if sled_weight < min_sled_weights[athlete_count]:
        return "Not Eligible"

    total = sled_weight + sum(athlete_weights)
    if total > max_weights[athlete_count]:
        return "Not Eligible"
    return "Eligible"
