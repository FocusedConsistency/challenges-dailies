def get_element_size(window_size, element_vw, element_vh):
    w, h = map(int, window_size.split(" x "))
    vw = int(element_vw[:-2]) / 100
    vh = int(element_vh[:-2]) / 100
    return f"{vw * w:g} x {vh * h:g}"

get_element_size("1000 x 500", "7vw", "3vh")
# "70 x 15"
