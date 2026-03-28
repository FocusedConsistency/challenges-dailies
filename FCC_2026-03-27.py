def truncate_text(s):
    widths = {
    **dict.fromkeys('.', 1),
    **dict.fromkeys('ilI', 1),
    **dict.fromkeys('fjrt ', 2),
    **dict.fromkeys('abcdeghkmnopqsuvwxyzJL', 3),
    **dict.fromkeys('ABCDEFGHKMNOPQRSTUVWXYZ', 4)
}

    total_width = 0
    result = []
    truncated = ""
    for char in s:
        total_width += widths.get(char, 0)
        print(total_width)
        if total_width > 50:
            return truncated
        elif total_width > 47:
            if not truncated:
                truncated = ''.join(result) + "..."
        result.append(char)

    return ''.join(result)
