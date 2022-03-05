def animals(heads, legs):
    chickens, cows = 2*heads-legs/2, legs/2-heads
    if chickens < 0 or cows < 0 or not chickens == int(chickens) or not cows == int(cows):
        return "No solutions"
    return chickens, cows


print(animals(72, 200))


def animals(heads, legs):
    chickens = heads * 2 - legs / 2
    cows = heads - chickens
    if chickens < 0 or cows < 0 or chickens != int(chickens):
        return "No solutions"
    return (chickens, cows)


print(animals(72, 200))
