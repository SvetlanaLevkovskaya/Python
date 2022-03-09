def dating_range(age):
    if age > 14:
        return '{}-{}'.format(int(age/2 + 7), int((age-7)*2))
    return '{}-{}'.format(int(age - 0.1*age), int(age + 0.1*age))


print(dating_range(17))
print(dating_range(13))
print(dating_range(14))


def dating_range(age):
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    else:
        min = (age / 2) + 7
        max = (age - 7) * 2

    return str(int(min)) + '-' + str(int(max))


print(dating_range(17))
print(dating_range(13))
print(dating_range(14))
