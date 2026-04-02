def fix_prank_number(arr):
    diffs = [b - a for a, b in zip(arr, arr[1:])]

    freq = {}
    max_count = 0
    most_common_diff = None
    for d in diffs:
        freq[d] = freq.get(d, 0) + 1
        if freq[d] > max_count:
            max_count = freq[d]
            most_common_diff = d

    result = []
    if len(freq) == 3:
        result.append(arr[0])
    elif len(freq) == 2:
        if arr[1] - arr[0] != most_common_diff:
            result.append(arr[1] - most_common_diff)
        else:
            result.append(arr[0])

    for num in range(1, len(arr)):
        result.append(result[num-1] + most_common_diff)

    return result
