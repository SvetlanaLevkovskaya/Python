"""Create a function that checks if a number n is divisible by two numbers x AND y.
All inputs are positive, non-zero digits."""


def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


print(is_divisible(12, 3, 4))


def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    return False


print(is_divisible(12, 3, 4))
