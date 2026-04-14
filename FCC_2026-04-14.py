def get_last_letter(s):
    last_char_index = -1
    last_num = -1
    for i, char in enumerate(s.lower()):
        if char.isalpha() and ord(char) > last_num:
            last_num = ord(char)
            last_char_index = i
    return s[last_char_index]
