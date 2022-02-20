""" Write a function that accepts two integers and returns the remainder
of dividing the larger value by the smaller value.
Division by zero should return an empty value."""


def remainder(a, b):
    if a > b and b == 0:
        return None
    if a < b and a == 0:
        return None
    if a == b and a == 0:
        return None
    if a < 0 and b == 0:
        return 0
    if a ==0 and b < 0:
        return 0
    if a < b:
        return b % a


print(remainder(0, -1))
print(remainder(-1, -1))
print(remainder(-1, 0))
print(remainder(1, 0))
print(remainder(0, 0))
print("*" * 60)


def remainder(a, b):
    if min(a, b) == 0:
        return None
    elif a > b:
        return a % b
    else:
        return b % a


print(remainder(0, -1))
print(remainder(-1, -1))
print(remainder(-1, 0))
print(remainder(1, 0))
print(remainder(0, 0))