from datetime import datetime

def get_day_of_week(timestamp):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    timestamp_s = timestamp / 1000
    dt = datetime.utcfromtimestamp(timestamp_s)
    day_number = dt.weekday()
    return days[day_number]
