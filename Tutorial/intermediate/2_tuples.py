# tuples: ordered, immutable, allows duplicate elements

mytuple = ()
print(mytuple)
print(type(mytuple))
mytuple = "Max", 28, "Boston"
print(mytuple)
mytuple = ("Max",)
print(mytuple)
print(type(mytuple))
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)
print(type(mytuple))

print('*'*80)
item = mytuple[0]
print('mytuple[0] = ', item)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")

print('*'*80)
my_tuple = ('a', 'p', 'p', 'l', 'e')
print('my_tuple = ', '                ', my_tuple)
print('len(my_tuple) = ', '           ', len(my_tuple))
print('my_tuple.count("p")', '        ', my_tuple.count("p"))
print('my_tuple.index("p")', '        ', my_tuple.index("p"))
my_list = list(my_tuple)
print('my_list = list(my_tuple)', '   ', my_list)
my_typle1 = tuple(my_list)
print('my_typle1 = tuple(my_list)', ' ', my_typle1)

print('*'*80)
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
print('a = ', '                       ', a)
print("a[2:5]", '                     ',  b)
b = a[2:]
print("a[2:]", '                      ',  b)
b = a[::2]
print("a[::2]", '                     ',  b)
b = a[::-1]
print("a[::-1]", '                    ',  b)

print('*'*80)
my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print("name, age, city = my_tuple", " ", my_tuple)
print('name = ', "                    ",  name)
print('age = ', "                     ",  age)
print('city = ', "                    ",  city)

print('*'*80)
my_tuple = (0, 1, 2, 3,4 )
i1, *i2, i3 = my_tuple
print("i1, *i2, i3 = my_tuple ", "    ", my_tuple)
print("i1 = ", "                      ", i1)
print("*i2 = ", "                     ", i2)
print("i3 = ", "                      ", i3)

print('*'*80)
import sys

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), bytes)
print(sys.getsizeof(my_tuple), bytes)

import timeit
print(timeit.timeit(stmt='[0,1,2,3,4,5,6,7,8,9,10]', number=1000000))
print(timeit.timeit(stmt='(0,1,2,3,4,5,6,7,8,9,10)', number=1000000))
