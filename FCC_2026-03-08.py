def is_valid_hsl(hsl):
    if hsl[:4] != "hsl(":
        return False
    stripped = "".join([x for x in hsl if x != " "])
    start = stripped.index("(")
    end = stripped.index(")")
    values = stripped[start+1:end].split(",")

    hue = int(values[0])
    sat = int(values[1][:-1])
    light = int(values[2][:-1])
    
    if values[1][-1] != "%" or values[2][-1] != "%":
        return False

    if hue < 0 or hue > 360 or sat < 0 or sat > 100 or light < 0 or light > 100:
        return False
    return True
