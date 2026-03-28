def pascal_row(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]

    triangle = [[1]]
    current_row = []
    for row_no in range(2, n + 1):
        last_row = triangle[-1]
        for index in range(row_no):
            if 0 < index < len(last_row):
                current_row.append(last_row[index - 1] + last_row[index])
            else:
                current_row.append(1)
        triangle.append(current_row.copy())
        current_row.clear()

    return triangle[-1]

pascal_row(10)
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

 #                   [1]
 #                 [1, 1]
 #               [1, 2, 1]
 #             [1, 3, 3, 1]
 #           [1, 4, 6, 4, 1]
 #         [1, 5, 10, 10, 5, 1]
 #       [1, 6, 15, 20, 15, 6, 1]
 #     [1, 7, 21, 35, 35, 21, 7, 1]
 #   [1, 8, 28, 56, 70, 56, 28, 8, 1]
 # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
