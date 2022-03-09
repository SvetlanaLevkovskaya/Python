"""Given a non-empty array of integers, return the result of multiplying the values together in order. """


def grow(arr):
    multiply = 1
    for x in arr:
        multiply *= x
    return multiply


print(grow([2, 3, 4]))
