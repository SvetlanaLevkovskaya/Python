# определить является ли число простым (простое число делится на себя и единицу: 2, 3, 5, 7, 11, 13,
a = int(input("Enter a number: "))
k = 0
delit = []

for i in range(1, a + 1):
    if a % i == 0:
        k += 1     # находим количество делителей нашего числа а
        delit.append(i)
if k == 2:
    print("Simple number")
else:
    print("It is not a simple number")
    print(delit)  # выводим все делители
