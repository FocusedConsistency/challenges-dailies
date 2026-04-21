def do_math(s):
    equation = []
    number = ""
    non_digit_count = 0
    for c in s:
        if c.isdecimal():
            number += c
            # Add operator based on non-digit count parity
            if equation and non_digit_count > 0:
                equation.append("+" if non_digit_count % 2 == 0 else "-")
                non_digit_count = 0
        else:
            # Process accumulated number
            if number:
                equation.append(str(int(number)))
                number = ""
            non_digit_count += 1

    if number:
        equation.append(str(int(number)))

    expr = ''.join(equation)
    print(expr)
    result = eval(expr) if equation else 0
    print(result)
    return result

do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt")
# 67-1-6-34+2-32-2-2-3-3-2+35-9+9+49-0+3+0-4
# 67
