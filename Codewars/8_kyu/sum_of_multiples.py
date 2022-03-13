"""Find the sum of all multiples of n below m
n and m are natural numbers (positive integers)
m is excluded from the multiples"""


def sum_mul(n, m):
    if n > 0 and m > 0:
        return sum(x for x in range(n, m) if x % n == 0)
    return 'INVALID'


print(sum_mul(3, 9))
print(sum_mul(2, -9))


def sum_mul(n, m):
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    return 'INVALID'


print(sum_mul(2, 9))
print(sum_mul(2, -9))


def sum_mul(n, m):
    return sum(x for x in range(n, m, n)) if n > 0 and m > 0 else 'INVALID'


print(sum_mul(2, 9))
print(sum_mul(2, -9))
