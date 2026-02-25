def find_differences(arr):
    result = []
    prev = arr[0]
    for curr in range(1, len(arr)):
        result.append(arr[curr] - prev)
        prev = arr[curr]
    result.append(0)
    return result

def find_differences(arr):
    return [curr - prev for prev, curr in zip(arr, arr[1:])] + [0]
