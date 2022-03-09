import string
from string import ascii_lowercase
print(ascii_lowercase)
print(string.digits)
print(string.printable)
print(string.hexdigits)


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}


def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)


print(alphabet_position("The sunset sets at twelve o' clock."))


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))


def alphabet_position(s):
    return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))


print(dir(str))
