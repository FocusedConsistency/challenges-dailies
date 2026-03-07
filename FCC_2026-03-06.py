def navigate_trail(map):
    moves = {        
        (0, 1): "R",
        (1, 0): "D",
        (0, -1): "L",
        (-1, 0): "U"
    }

    curr_pos = (0, 0)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "C":
                    curr_pos = (i, j)

    def is_valid_move(pos):
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(map) and pos[1] < len(map[0])

    map_li = []
    for row in map:
        map_li.append(list(row))

    result = []
    fin = False
    count = 0

    while map_li[curr_pos[0]][curr_pos[1]] != "G" and fin == False and count < 100:
        for move in moves:
            new_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
            if is_valid_move(new_pos):
                if map_li[new_pos[0]][new_pos[1]] == "G":
                    result.append(moves[move])
                    fin = True
                    break
                if map_li[new_pos[0]][new_pos[1]] == "T":
                    result.append(moves[move])
                    map_li[curr_pos[0]][curr_pos[1]] = "-"
                    map_li[new_pos[0]][new_pos[1]] = "C"
                    curr_pos = new_pos
                    break
        count += 1
    return ''.join(result)

navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"])
# "ULLLUUURRRRRRDDDR"
