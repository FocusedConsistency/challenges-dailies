def is_valid_domino_chain(dominoes):
    prev = dominoes[0][1]
    for dom in dominoes[1:]:
        if dom[0] != prev:
            return False
        prev = dom[1]
    return True
