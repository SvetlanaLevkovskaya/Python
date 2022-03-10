from collections import Counter


def char_freq(message):
    return Counter(message)


print(char_freq("I like cats"))


def char_freq(message):
    result = {}
    for letter in message:
        result[letter] = result.get(letter, 0) + 1
    return result


print(char_freq("I like cats"))
