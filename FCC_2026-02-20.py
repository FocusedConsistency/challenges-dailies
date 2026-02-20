def is_valid_trick(trick_name):
    valid_first = {"Misty",
        "Ghost",
        "Thunder",
        "Solar",
        "Sky",
        "Phantom",
        "Frozen",
        "Polar"
    }
    valid_second = {"Twister",
        "Icequake",
        "Avalanche",
        "Vortex",
        "Snowstorm",
        "Frostbite",
        "Blizzard",
        "Shadow"}
    if not trick_name or not isinstance(trick_name, str):
        return False

    names = trick_name.strip().split()

    if len(names) != 2:
        return False

    return names[0] in valid_first and names[1] in valid_second
