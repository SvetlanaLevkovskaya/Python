def stringy(size):
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(len(size))])


print(stringy('johnMcClane'))


def stringy(size):
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(size)])


print(stringy(10))


def stringy(size):
    return "".join([str(i % 2) for i in range(1, size + 1)])


print(stringy(10))


def stringy(size):
    return ('10' * size)[:size]


print(stringy(10))
