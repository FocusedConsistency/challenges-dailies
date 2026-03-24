def has_no_repeats(s):
    if not s:
        return True

    prev = None
    for char in s:
        if char == prev:
            return False
        prev = char
    return True

has_no_repeats("The quick brown fox jumped over the lazy dog.")
# True
