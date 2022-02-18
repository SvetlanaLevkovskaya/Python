def high_and_low(numbers):
    return ' '.join(x(numbers.split(), key=int) for x in (max, min))


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
