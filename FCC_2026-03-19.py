def invert_matrix(matrix):
    if not matrix:
        return matrix
        
    val_1 = matrix[0][0]

    def find_second_value():
        for array in matrix:
            for x in array:
                if x != val_1:
                    return x
        return None

    val_2 = find_second_value()

    # All values are the same, no need to invert
    if val_2 is None:
        return matrix

    for array in matrix:
        for j in range(len(array)):
            if array[j] == val_1:
                array[j] = val_2
            elif array[j] == val_2:
                array[j] = val_1

    return matrix

invert_matrix([
  [6, 7, 7, 7, 6], 
  [7, 6, 7, 6, 7], 
  [7, 7, 6, 7, 7], 
  [7, 6, 7, 6, 7], 
  [6, 7, 7, 7, 6]
])

# [[7, 6, 6, 6, 7], 
#  [6, 7, 6, 7, 6], 
#  [6, 6, 7, 6, 6], 
#  [6, 7, 6, 7, 6], 
#  [7, 6, 6, 6, 7]]
