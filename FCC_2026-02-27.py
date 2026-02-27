def shift_matrix(matrix, shift):
    count = len(matrix) * len(matrix[0])
    shifted = shift

    if abs(shift) > count:
        shifted = abs(shift) % count
        if shift < 0:
            shifted *= (-1)

    new_list = [0] * count
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            new_in = shifted+j+i*len(row)
            if new_in >= len(new_list):
                new_in -= len(new_list)
            new_list[new_in] = matrix[i][j]

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            matrix[i][j] = new_list[j+i*len(row)]
        
    return matrix

shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54)
# [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]]
