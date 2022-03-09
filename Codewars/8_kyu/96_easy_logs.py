"""Add two logs with base X, with the value of A and B. Example log A + log B where the base is X."""

from math import log


def logs(x, a, b):
    return log(a,x) + log(b,x)



print(logs(10, 2, 3))


def logs(x, a, b):
    return log(a*b, x)


print(logs(10, 2, 3))