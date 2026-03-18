def largest_number(s):
    numbers = []
    current = []
    for char in s:
        if char.isdecimal() or char in "-.":
            current.append(char)
        else:
            num = "".join(current)
            numbers.append(float(num))
            current.clear()
    num = "".join(current)
    numbers.append(float(num))
    return max(numbers)
