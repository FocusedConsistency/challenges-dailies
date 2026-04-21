def sort_and_swap(arr):
    sorted_arr = sorted(arr)
    result_arr = []
    for i, num in enumerate(sorted_arr):
        if i % 3 == 0:
            result_arr.insert(i-1, num)
        else:
            result_arr.append(num)
    return result_arr

sort_and_swap([1, 2, 3, 4, 5, 6, 7, 8, 9])
# [1, 2, 4, 3, 5, 7, 6, 8, 9]
