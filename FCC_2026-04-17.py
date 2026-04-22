def decode(message):
    key = "VLHCGMDLNH"
    key_val = 0
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for char in message:
        if char in alpha:
            char_index = alpha.find(char)
            shift = alpha.find(key[key_val]) + 1
            key_val += 1
            if key_val >= 10:
                key_val = 0
            shifted = char_index - shift
            if shifted < 0:
                shifted += len(alpha)
            result.append(alpha[shifted])
        else:
            result.append(char)     
    return ''.join(result)

decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB")
# "A WINNER IS A DREAMER WHO NEVER GIVES UP"
