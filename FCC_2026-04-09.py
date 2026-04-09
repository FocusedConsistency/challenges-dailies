import bisect

def get_next_bingo_number(n):
    num = int(n[1:]) + 1
    if num > 75:
        num -= 75
    breakpoints = [15, 30, 45, 60, 75]
    letters = ['B', 'I', 'N', 'G', 'O']
    index = bisect.bisect_right(breakpoints, num)
    return letters[index] + str(num)
