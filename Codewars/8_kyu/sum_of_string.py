"""Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
If either input is an empty string, consider it as zero."""


def sum_str(a, b):
    if a == "":
        a = 0
    if b == "":
        b = 0
    return str(int(a) + int(b))


print(sum_str("", ""))
print(sum_str("9", ""))
print(sum_str("", "9"))
print(sum_str("9", "9"))


def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


print(sum_str("", ""))
print(sum_str("9", ""))
print(sum_str("", "9"))
print(sum_str("9", "9"))
