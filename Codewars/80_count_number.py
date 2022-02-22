"""monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monkeyCount(1) # --> [1]"""


def monkey_count(n):
    return list(range(1, n+1))


print(monkey_count(10))
