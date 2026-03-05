def smallest_gap(s):
    if not s:
        return s

    char_indices = {}
    for index, char in enumerate(s):
        char_indices.setdefault(char, []).append(index)

    min_gap = float('inf')
    min_index = float('inf')
    max_index = float('inf')
    for key, value in char_indices.items():
        if len(value) < 2:
            continue
        for i in range(1, len(value)):
            prev = value[i - 1]
            curr = value[i]
            gap = curr - prev - 1
            if gap < min_gap or (gap == min_gap and prev < min_index):
                min_index = prev
                max_index = curr
                min_gap = gap

    if min_gap == float('inf'):
        return s
    return s[min_index + 1:max_index]

print(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"))
# #q6e&rkf(p
print(smallest_gap("The quick brown fox jumps over the lazy dog."))
# fox
