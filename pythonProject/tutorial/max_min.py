a = input('first number: ')
b = input('second number: ')
c = input('third number: ')

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

if a < b:
    if a < c:
        print(a)
    else:
        print(b)
else:
    if b < c:
        print(b)
    else:
        print(c)
