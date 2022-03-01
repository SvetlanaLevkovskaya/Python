"""Jack really likes his number five: the trick here is that you have to multiply each number
by 5 raised to the number of digits of each numbers, so, for example:
multiply(3)==15 # 3 * 5¹
multiply(10)==250 # 10 * 5²
multiply(200)==25000 # 200 * 5³
multiply(0)==0 # 0 * 5¹
multiply(-3)==-15 # -3 * 5¹
"""


def multiply(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return 5**count


print(multiply(10))
print(multiply(5))
print(multiply(0))
print(multiply(200))


def multiply(n):
    return n*5**len(str(abs(n)))


print(multiply(10))
print(multiply(5))
print(multiply(0))
print(multiply(200))
