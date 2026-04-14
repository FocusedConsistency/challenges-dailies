def spiral_matrix(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    total_length = row_count * col_count
    result = []
    i = 0
    j = -1
    positions = []

    while len(result) != total_length:
        while j < col_count - 1:
            j += 1
            pos = (i, j)
            if pos not in positions:
                result.append(matrix[i][j])
                positions.append(pos)
            else:
                j -= 1
                break
        while i < row_count - 1:
            i += 1
            pos = (i, j)
            if pos not in positions:
                result.append(matrix[i][j])
                positions.append(pos)
            else:
                i -= 1
                break
        while j > 0:
            j -= 1
            pos = (i, j)
            if pos not in positions:
                result.append(matrix[i][j])
                positions.append(pos)
            else:
                j += 1
                break
        while i > 0:
            i -= 1
            pos = (i, j)
            if pos not in positions:
                result.append(matrix[i][j])
                positions.append(pos)
            else:
                i += 1
                break
    return result

spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]])

# ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"].
