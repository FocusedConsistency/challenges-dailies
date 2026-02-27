def shift_matrix(matrix, shift):
    rows = len(matrix)
    cols = len(matrix[0])
    total = rows * cols
    shift %= total

    new_list = [0] * total
    cols = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            original_index = i * cols + j
            index = (original_index + shift) % total
            new_list[index] = matrix[i][j]

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            matrix[i][j] = new_list[i * cols + j]

    return matrix

shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54)
# [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]]

def shift_matrix_2(matrix, shift):
    rows = len(matrix)
    cols = len(matrix[0])
    total = rows * cols
    shift %= total

    flattened = [matrix[i][j] for i in range(rows) for j in range(cols)]
    
    shifted = flattened[-shift:] + flattened[:-shift]
    
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = shifted[i * cols + j]
    
    return matrix

shift_matrix_2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54)
# [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]]
