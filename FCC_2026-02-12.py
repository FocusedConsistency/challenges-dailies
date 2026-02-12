def largest_difference(skater1, skater2):
    max_diff = -1
    lap_of_max = 0
    for i, (sk1_lap, sk2_lap) in enumerate(zip(skater1, skater2)):
        diff = abs(sk1_lap - sk2_lap)
        if diff > max_diff:
            max_diff = diff
            lap_of_max = i + 1
    return lap_of_max

largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]) # should return 3
