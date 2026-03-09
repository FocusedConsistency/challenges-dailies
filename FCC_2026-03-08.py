def is_valid_hsl(hsl):
    if not hsl.startswith("hsl(") or not hsl.endswith((")", ";")):
        return False

    stripped = hsl.replace(" ", "")

    try: 
        start = stripped.index("(") + 1
        end = stripped.index(")")
    except ValueError as e:
        print(f"Invalid bracket syntax: {e}")
        return False

    values = stripped[start:end].split(",")

    if len(values) != 3:
        return False
    if values[1][-1] != "%" or values[2][-1] != "%":
        return False

    try:
        hue = int(values[0])
        sat = int(values[1][:-1])
        light = int(values[2][:-1])
    except ValueError as e:
        print(f"Invalid hsl values: {e}")
        return False   

    if hue < 0 or hue > 360 or sat < 0 or sat > 100 or light < 0 or light > 100:
        return False
    return True

is_valid_hsl("hsl(240, 50%, 50%)")
