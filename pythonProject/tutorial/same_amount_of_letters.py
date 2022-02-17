def xo(s):
    return s.lower().count('x') == s.lower().count('o')


print(xo('XXoo'))
print(xo('TR'))


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo('TRxxoo'))