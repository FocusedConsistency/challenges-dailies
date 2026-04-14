def rook_bishop_attack(rook, bishop):
    rook_char, rook_num = rook[:1], rook[1:]
    bishop_char, bishop_num = bishop[:1], bishop[1:]
    if rook_char == bishop_char or rook_num == bishop_num:
        return "rook"

    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    char_diff = abs(letters.index(rook_char) - letters.index(bishop_char))
    num_diff = abs(int(rook_num) - int(bishop_num))
    if char_diff == num_diff:
        return "bishop"
    return "neither"

rook_bishop_attack("B7", "H1")
# bishop
