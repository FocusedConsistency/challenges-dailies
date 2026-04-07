def get_rotation(n):
    num = n
    length = len(str(n))
    for i in range(length):
        if num % length == 0:
            print(f"{num} divisible by {i}")
            return i
        num = int(str(num)[1:]+str(num)[0])
    return "none"

get_rotation(84138789345)
# 6
# 89345841387 divisible by 6
