a = int(input('Enter a year: '))
if (a % 4 == 0 and a != 0) or a % 400 == 0:
    print(a, " - високосный год")
else:
    print(a, " - не високосный год")
