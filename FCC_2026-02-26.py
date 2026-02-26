def count_letters_and_numbers(s):
    letters = numbers = 0
    for char in s:
        if char.isalpha():
            letters += 1
        if char.isdecimal():
            numbers += 1

    return f"The string has {letters} letter{'' if letters==1 else 's'} and {numbers} number{'' if numbers == 1 else 's'}."

count_letters_and_numbers("helloworld123")
# returns "The string has 10 letters and 3 numbers.".
