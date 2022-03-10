a = int(input('enter number a: '))
b = int(input('enter number b: '))

while a != 0 and b !=0:
    if a > b:
        a %= b    # a = a % b
    else:
        b %= a    # b = b % a
# print(a)
# print(b)
print(a + b)
