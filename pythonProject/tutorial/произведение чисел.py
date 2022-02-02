# найти произведение всех четных чисел от 1 до 100
p = 1
for i in range(1, 6+1):
    if i % 2 == 0:
        p = p * i
print(i, p)

# сумма
s = 0
for i in range(1, 100+1):
    if i % 2 == 0:
        s += i  # s = s + i
print(i, s)

# среднеарифметическое

s = 0
k = 0
for i in range(1, 100+1):
    if i % 2 == 0:
        s += i
        k += 1
print(s, k, s/k)
print(2550//50)
print(2550/50)

# найти самое большое число которое делиться на 2 и на 3
max = 1
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        if i > max:
            max = i
print(max)

min = 100
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        if i < min:
            min = i
print(min)



