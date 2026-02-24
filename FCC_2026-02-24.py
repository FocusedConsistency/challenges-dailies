from datetime import datetime, timedelta

def count_business_days(start, end):
    start = datetime.strptime(start, '%Y-%m-%d')
    end = datetime.strptime(end, '%Y-%m-%d')

    current = start
    b_days = 0
    while current <= end:
        if current.weekday() < 5:
            b_days += 1
        current += timedelta(days=1)
    return b_days
