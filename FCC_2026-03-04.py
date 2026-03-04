def card_values(cards):
    if not cards:
        return result
        
    result = []
    faces = {"J", "Q", "K"}
    for card in cards:
        value = 0
        value_str = card[:-1]
        if value_str == "A":
            value = 1
        elif value_str in faces:
            value = 10
        else:
            value = int(value_str)
        result.append(value)
    return result
