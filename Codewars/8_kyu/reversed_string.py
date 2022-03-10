def reverseWords(str):
    return " ".join(str.split(" ")[::-1])


print(reverseWords('Hello world!'))


def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))


print(reverseWords('Hello world!'))
