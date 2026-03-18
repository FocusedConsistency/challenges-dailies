def largest_number(s):
    numbers = []
    current = []
    
    def append_current():
        num = "".join(current)
        numbers.append(float(num))
        
    for char in s:
        if char.isdecimal() or char in "-.":
            current.append(char)
        else:
            append_current()
            current.clear()
    append_current()
    return max(numbers)
