def get_difficulty(track):
    if not track:
        raise ValueError("No track provided")

    score = 0
    if track[0] in 'LR':
        score += 5
    for prev, curr in zip(track, track[1:]):
        if curr in 'LR':
            score += 5
            if prev != curr and prev in 'LR':
                score += 10
    if score > 200:
        return "Hard"
    if score > 100:
        return "Medium"
    return "Easy"

get_difficulty("SLSLLSRRLSRLRL") # should return "Easy".
