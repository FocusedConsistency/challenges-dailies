def capitalize_fibonacci(s):
    fib = [0, 1]
    while fib[-1] < len(s):
        fib.append(fib[-2] + fib[-1])

    li = list(s.lower())
    for i, char in enumerate(li):
        if i in fib:
            li[i] = char.upper()

    return "".join(li)

capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl.") 
# "LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl."
