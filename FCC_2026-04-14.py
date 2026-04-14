def get_initials(name):
    names = name.split()
    initials = []
    for n in names:
        initials.append(n[0])
    return ".".join(initials) + "."

get_initials("Tommy Millwood")
