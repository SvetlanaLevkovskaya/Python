""" function takes two arguments:
current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old)."""


def twice_as_old(dad_years_old, son_years_old):
    twice = (dad_years_old - son_years_old) * 2
    return abs(dad_years_old - twice)


print(twice_as_old(55, 10))
print(twice_as_old(29, 0))
print(twice_as_old(36, 7))


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)


print(twice_as_old(55, 10))
print(twice_as_old(29, 0))
print(twice_as_old(36, 7))