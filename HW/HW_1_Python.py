# 1) Создать переменную типа String
name = 'Svetlana'
surname = str('Levkovskaya')
print(name, type(name))
print(surname, type(surname))

# 2) Создать переменную типа Integer
age = '42'
print(age, type(age))

# 3) Создать переменную типа Float
prof = '0.1'
print(prof, type(prof))

# 4) Создать переменную типа Bytes
x = b'Hello'
print(x, type(x))

z = 'Svetlana'
v = z.encode()
print(v, type(v))

# 5) Создать переменную типа List
my_list = ["apple", "banana", "cherry", "banana"]
my_list_1 = ["abc", 34, True, 40, "male"]
print(my_list, type(my_list))
print(my_list_1, type(my_list_1))
print(len(my_list_1))

# 6) Создать переменную типа Tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple, type(my_tuple))
print(len(my_tuple))

# 7) Создать переменную типа Set
# // Set items are unordered, unchangeable, and do not allow duplicate values.Set items can be of any data type
# set1 = {"abc", 34, True, 40, "male"}
my_set = {"apple", "banana", "cherry"}
print(my_set, type(my_set))
print(len(my_set))

# 8. Создать переменную типа Frozen set
my_set_1 = {"apple", "banana", "cherry"}
fset = frozenset(my_set_1)
print(fset, type(fset))

my_set_2 = frozenset({"apple", "banana", "cherry"})
print(my_set_2, type(my_set_2))

my_set_3 = frozenset(("apple", "banana", "cherry"))
print(my_set_3, type(my_set_3))

# 9) Создать переменную типа Dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict,type(thisdict))
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
name = 'Svetlana'
surname = 'Levkovskaya'
fullname = name + surname
print(fullname, type(fullname))

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
a = 10
b = 20
c = a + b
print(c)

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
a = 10
b = 20
c = a / b
print(c)
# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
a = 10
b = 20
c = a * b
print(c)

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
a = 11
b = 4
c = a % b
print('c = ', c)
# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
x = 11
x%=4
print('x = ', x)

# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
z = (7 + 12) ** 3 + 7 * 4 - 44 / 2**4
print('z = ', z)

# random
import random
print(random.randrange(1, 100))

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# loop
for x in "banana":
  print(x)

# Check the string
txt = "The best things in life are free!"
print("free" in txt)

