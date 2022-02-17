sheep = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];

count = 0
for i in sheep:
    if i:
        count += 1
print(count)


def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count


print(count_sheeps(sheep))


def count_sheeps(sheep):
    return sheep.count(True)


print(count_sheeps(sheep))
