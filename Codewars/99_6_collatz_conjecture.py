"""hotpo(1) returns 0
(1 is already 1)

hotpo(5) returns 5
5 -> 16 -> 8 -> 4 -> 2 -> 1

hotpo(6) returns 8
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

hotpo(23) returns 15
23 -> 70 -> 35 -> 106 -> 53 -> 160 -> 80 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1"""


def hotpo(num, count=0):
    return count if num == 1 else hotpo(num / 2 if num % 2 == 0 else num * 3 + 1, count + 1)


print(hotpo(1))
print(hotpo(10))


def hotpo(n):
    count = 0
    while n != 1:
      n = 3 * n + 1 if n % 2 else n / 2
      count += 1
    return count


print(hotpo(1))
print(hotpo(10))
