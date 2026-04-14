def rook_attack(rook1, rook2):
    if rook1[:1] == rook2[:1] or rook1[1:] == rook2[1:]:
        return True
    return False
