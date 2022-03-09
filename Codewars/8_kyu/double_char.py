def double_char(s):
    return ''.join(x+x for x in s)


print(double_char('string'))


def double_char(s):
    return ''.join(c * 2 for c in s)


print(double_char('string'))
