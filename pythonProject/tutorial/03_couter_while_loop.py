# inhabitants = 1000
# counter = 0
# while inhabitants < 1200:
#     inhabitants= int(inhabitants * 1.02 + 50)
#     counter +=1
# print(inhabitants_count, counter)


def nb_year(p0, percent, aug, p):
    counter = 0
    while p0 < p:
        p0 = int(p0 + p0 * percent/100 + aug)
        counter += 1
    print(counter)


nb_year(1000, 1.2, 50, 1200)


def nb_year(p0, percent, aug, p):
    t = 0
    while p0 < p:
        p0 = int(p0*(1 + percent/100)) + aug
        t += 1
    return t


def nb_year(p0, percent, aug, p, years=0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years


print(nb_year(1500000, 0.25, 1000, 2000000, 0))
