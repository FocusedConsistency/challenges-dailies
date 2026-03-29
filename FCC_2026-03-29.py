def is_valid_isbn10(s):
    digits = ''.join(s.split("-"))
    if len(digits) != 10:
        return False

    total = 0
    for i, digit in enumerate(digits[:-1]):
        if not digit.isdecimal():
            return False
        else:
            total += int(digit) * (i+1)
    
    last_digit = digits[-1]
    if not (last_digit.isdecimal() or last_digit == "X"):
        return False
    elif last_digit.isdecimal():
        total += int(last_digit) * 10
    elif last_digit == "X":
        total += 10 * 10

    return not total % 11

is_valid_isbn10("0-306-40615-2")
# True
