def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


print(feast("brown bear", "bear claw"))


def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])


print(feast("brown bear", "bear claw"))
