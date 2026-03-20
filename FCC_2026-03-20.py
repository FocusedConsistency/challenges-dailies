def get_shadow(time):
    h, m = time.split(':')
    hours = int(h) + int(m) / 60

    if hours < 6 or hours >= 18 or hours == 12:
        return "No shadow"
    
    direction = 'west' if hours < 12 else 'east'
    length = abs(12 - hours) ** 3
    return f"{int(length) if length.is_integer() else length}ft {direction}"
