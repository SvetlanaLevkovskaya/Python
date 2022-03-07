def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


print(feast("brown bear", "bear claw"))


def name_shuffler(str_):
    s = str_.split()
    return ''.join('{} {}'.format(s[1], s[0]))


print(name_shuffler('john McClane'))
