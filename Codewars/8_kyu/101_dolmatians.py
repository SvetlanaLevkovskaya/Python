def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <= 10:
        return dogs[0]
    elif n <= 50:
        return dogs[1]
    elif n == 101:
        return dogs[3]
    return dogs[2]


print(how_many_dalmatians(22))


def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if n <= 10 else dogs[1] if n <= 50 else dogs[3] if n == 101 else dogs[2]


print(how_many_dalmatians(22))
