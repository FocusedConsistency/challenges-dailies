def get_due_date(date_str):
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31

    }

    y, m, d = map(int, date_str.split("-"))
    m += 9
    if m > 12:
        m -= 12
        y += 1
    if months[m] < d:
        d = months[m]
    return f"{y}-{m:02d}-{d}"
