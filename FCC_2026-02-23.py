def score_curling(house):
    def get_ring(i, j):
        if i == 2 and j == 2:
            return 0
        elif max(abs(i - 2), abs(j - 2)) == 1:
            return 1
        else:
            return 2

    r_stones = []
    y_stones = []
    for i in range(5):
        for j in range(5):
            if house[i][j] == 'R':
                r_stones.append(get_ring(i, j))
            elif house[i][j] == 'Y':
                y_stones.append(get_ring(i, j))

    if min(r_stones) < min(y_stones):
        points = sum(x < min(y_stones) for x in r_stones)
        return f'R: {points}'
    elif min(r_stones) > min(y_stones):
        points = sum(x < min(r_stones) for x in y_stones)
        return f'Y: {points}'

    return "No points awarded"

score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]])
# Returns "R:2"
# [
#     [".", ".", "R", ".", "."], 
#     [".", "R", ".", ".", "."], 
#     ["Y", ".", ".", ".", "."], 
#     [".", "R", ".", ".", "."], 
#     [".", ".", ".", ".", "."]
# ]
