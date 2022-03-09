def reverse_words(text):
    new_text = []
    for word in text.split():    # split all spaces
        new_text.append(word[::-1])
    return ' '.join(new_text)


print(reverse_words('double  spaced  words'))


def reverse_words(text):
    new_text = []
    for word in text.split(" "):      # split only one space
        new_text.append(word[::-1])
    return ' '.join(new_text)


print(reverse_words('double  spaced  words'))


def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


print(reverse_words('double  spaced  words'))
