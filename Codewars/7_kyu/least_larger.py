"""Given an array of numbers and an index, return the index of the least number larger than the element
at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value )."""


def least_larger(a, i):
    b = [x for x in a if x > a[i]]
    return a.index(min(b)) if b else -1


print(least_larger([4, 1, 3, 5, 6], 0))
