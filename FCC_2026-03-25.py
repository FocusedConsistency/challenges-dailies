from datetime import datetime

def can_retake(finish_time, current_time):
    fin = datetime.fromisoformat(finish_time)
    curr = datetime.fromisoformat(current_time)
    difference = curr - fin
    return difference.total_seconds() / 3600 >= 48

can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00")
# True
