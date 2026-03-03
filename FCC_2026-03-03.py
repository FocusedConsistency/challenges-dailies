def count_perfect_cubes(a, b):
    mini = min(a, b)
    maxi = max(a, b)
    count = 0
    i = 0
    cube = 0
    while cube < maxi:
        cube = i * i * i
        if mini <= cube <= maxi:
            count += 1
        i += 1

    if mini < 0:
        i = -1
        cube = 0
        while cube > mini:
            cube = i * i * i
            if cube >= mini:
                count += 1
            i -= 1

    return count

count_perfect_cubes(9214, -8127)
# 41
