def sequence(x):
    return sorted(range(1, x+1), key=str)


print(sequence(10))


def sequence(x):
    return [int(i) for i in sorted([str(n) for n in range(1, x+1)])]


print(sequence(10))
