from math import ceil

def round_it(n):
    left, right = (len(part) for part in str(n).split("."))
    return ceil(n) if left < right else int(n) if left > right else round(n)


print(round_it(3.45))
print(round_it(34.5))
print(round_it(34.56))