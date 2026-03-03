def count_perfect_cubes(a, b):
    mini = min(a, b)
    maxi = max(a, b)

    i = round(abs(mini) ** (1/3))
    if mini < 0:    
        i *= -1
    i -= 1

    count = 0
    while True:
        cube = i * i * i
        if cube > maxi:
            break
        if cube >= mini:
            count += 1
        i += 1
    return count

print(count_perfect_cubes(-1, 0))  # 2
print(count_perfect_cubes(0, 0))  # 1
print(count_perfect_cubes(0, 1))  # 2
print(count_perfect_cubes(-1, 1))  # 3
print(count_perfect_cubes(9214, -8127))  # 41
print(count_perfect_cubes(10**18, 10))  # 999998
print(count_perfect_cubes(-10**18, 10**18))  # 2000001
