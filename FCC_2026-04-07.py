def palindrome_locator(s):
    length = len(s)
    index = length // 2
    if s == s[::-1]:
        if length % 2 == 1:
            return s[index]
        else:
            return s[index - 1:index + 1]
    return "none"
