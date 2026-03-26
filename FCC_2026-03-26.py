def get_movie_night_cost(day, showtime, number_of_tickets):
    days = {
        "Monday": 10,
        "Tuesday": 5,
        "Wednesday": 10,
        "Thursday": 10,
        "Friday": 12,
        "Saturday": 12,
        "Sunday": 12
    }
    total = days[day]
    if day == "Tuesday":
        return f"${number_of_tickets * total:.2f}"
    if showtime[-2:] == "am" or int(showtime.split(":")[0]) < 5:
        total -= 2
    return f"${number_of_tickets * total:.2f}"

get_movie_night_cost("Monday", "11:50am", 4)
# "$32.00"
