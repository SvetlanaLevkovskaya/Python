# найти сумму цифр введенного числа
# a = int(input("Enter a number: "))
# s = 0
# while a > 0:
#     s += a % 10
#     a = a // 10
# print(s)


a = int(input("Enter a number: "))
s = 1
while a > 0:
    s *= a % 10
    a = a // 10
print(s)