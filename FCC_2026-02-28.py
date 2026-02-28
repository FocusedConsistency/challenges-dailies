def add_punctuation(sentences):
    li = []
    for i, item in enumerate(sentences):
        if item.isupper() and sentences[i-1] == ' ':
            li.insert(-1, '.')
        li.append(item)

    li.append('.')
    return ''.join(li)

add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z")
# "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z."
