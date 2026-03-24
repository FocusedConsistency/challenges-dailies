def detect_roast(beans):
    roasts = {
        "'": 1,
        "-": 2,
        ".": 3
    }
    score = 0
    for roast in beans:
        score += roasts[roast]
    
    avg = score / len(beans)
    if avg < 1.75:
        return "Light"
    if avg <= 2.5:
        return "Medium"
    return "Dark"

detect_roast(".--.-..-......----.'")
# "Medium"
