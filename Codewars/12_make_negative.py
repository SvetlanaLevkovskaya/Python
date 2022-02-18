def make_negative(number):
    if number < 0:
        return number
    return number * -1


print(make_negative(-42))
print(make_negative(42))


def make_negative(number):
    return -abs(number)


print(make_negative(-52))
print(make_negative(52))


def make_negative(number):
    return -number if number > 0 else number


print(make_negative(-62))
print(make_negative(62))