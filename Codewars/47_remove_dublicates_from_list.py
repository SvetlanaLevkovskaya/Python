"""Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same."""


def distinct(seq):
    return list(dict.fromkeys(seq))


print(distinct([1, 1, 2]))


def distinct(seq):
    return list(set(seq))


print(distinct([1, 1, 2]))
