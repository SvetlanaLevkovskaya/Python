import math
def litres(time):
    """ Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink,
rounded to the smallest value."""
    return math.floor(time * 60 * 0.5/60)


print(litres(1))


def litres(time):
    return time // 2


print(litres(1))
