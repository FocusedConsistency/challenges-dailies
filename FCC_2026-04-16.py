def do_math(s):
    equation = []
    number = ""
    non_digit_count = 0
    for c in s:
        if c.isdecimal():
            number += c
            if len(equation) > 0 and non_digit_count > 0:
                if non_digit_count % 2 == 0:
                    equation.append("+")
                else:
                    equation.append("-")
                non_digit_count = 0
        else:
            if len(number) > 0:
                equation.append(str(int(number)))
                number = ""
            non_digit_count += 1
    if len(number) > 0:
        equation.append(str(int(number)))
    print(''.join(equation))
    print(eval(''.join(equation)))
    return eval(''.join(equation))

do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt")
# 67-1-6-34+2-32-2-2-3-3-2+35-9+9+49-0+3+0-4
# 67
