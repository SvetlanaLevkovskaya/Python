from math import sqrt


def square_or_square_root(arr):
    return [int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr]


print(square_or_square_root([4, 3, 9, 7, 2, 1]))


def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(round(root))
        else:
            result.append(x*x)
    return result


print(square_or_square_root([4, 3, 9, 7, 2, 1]))
