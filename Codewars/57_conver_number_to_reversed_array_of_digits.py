"""Given a random non-negative number, you have to return
the digits of this number within an array in reverse order."""


def digitize(n):
    return [int(x) for x in str(n)][::-1]


print(digitize(23582357))
