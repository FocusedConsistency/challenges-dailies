def truncate_text(s):
    widths = [(".", 1), ("ilI", 1), ("fjrt", 2), (" ", 2), ("abcdeghkmnopqrstuvwxyzJL", 3), ("ABCDEFGHKMNOPQRSTUVWXYZ", 4)]
    def check_width(char):
        for width in widths:
            if char in width[0]:
                return width[1]
        return 0

    total_width = 0
    new_s = []
    for char in s:
        total_width += check_width(char)
        if total_width > 47:
            new_s.append("...")
            return ''.join(new_s)
        new_s.append(char)

    return ''.join(new_s)

truncate_text("THE LOUD BRIGHT BIRD")
# "THE LOUD BRIG..."
