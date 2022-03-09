""" If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'.
If there are no good ideas,
as is often the case, return 'Fail!'."""


def well(x):
    if x.count('good') == 1 or x.count('good') == 2:
        return "Publish!"
    elif x.count('good') > 2:
        return "I smell a series!"
    return "Fail!"


print(well(['bad', 'bad', 'bad', 'bad', 'bad', 'bad',]))
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'good']))


def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


print(well(['bad', 'bad', 'bad', 'bad', 'bad', 'bad',]))
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'good']))
