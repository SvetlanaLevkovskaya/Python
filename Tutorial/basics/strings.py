# Дана строка. Написать метод, которых находит сумму всех цифр в строке (например для “abc3d4e asdf12” - ответ 10)
a = 'abc3d4e asdf12'
count = 0
for x in a:
    if x.isdigit():
        count += int(x)
print("sum =", count)


def sum_digits(a):
    return sum(int(x) for x in a if x.isdigit())


print(sum_digits('abc3d4e asdf12'))


def sum_digits(a):
    return ', '.join(x for x in a if x.isalpha())


print(sum_digits('abc3d4e asdf12'))

a = 'abc3d4e asdf12'
print(a.split())

help(str)

print(ord('A'))

print('A\nB\tC')
print(len('A\nB\tC'))
print(len('\n'))

print('A\0B\0C')
print(len('A\0B\0C'))




