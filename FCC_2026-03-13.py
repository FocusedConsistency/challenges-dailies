import math

def calculate_parking_fee(park_time, pickup_time):
    park_min = 60 * int(park_time[:2]) + int(park_time[3:])
    pickup_min = 60 * int(pickup_time[:2]) + int(pickup_time[3:])

    cost = 0
    parked_time = 0
    minutes_in_a_day = 1440
    if pickup_min > park_min:
        parked_time = pickup_min - park_min
    else:
        parked_time = minutes_in_a_day - park_min + pickup_min
        cost += 10

    if parked_time < 60:
        return "$5"

    cost += math.ceil(parked_time / 60) * 3
    return f"${cost}"

calculate_parking_fee("18:15", "01:30")
# $34
calculate_parking_fee("11:11", "11:10")
# $82
