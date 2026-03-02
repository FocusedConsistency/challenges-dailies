def sum_letters(s):
    return sum(ord(char.lower()) - ord('a') + 1 for char in s if char.isalpha())

sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.") 
# 1681
