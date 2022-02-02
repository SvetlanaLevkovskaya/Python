name = 'bro'
age = 21
age += 1
print(age)
print('My name:' + str(age))

height = 250.5
print(type(height))
print('My height ' + str(height) + ' cm')

human = False
print(type(human))
print('Are you a human? ' + str(human))

name, age, attractive = 'Bro', 21, True

print(age)
print(name)
print(attractive)


# Sponchbob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# multiple assignment

Sponchbob = Patrick = Sandy = Squidward = 30


print(Sponchbob)
print(Patrick)
print(Sandy)
print(Squidward)

print('________________________________')

name = "Svetlana"
print(len(name))
print(name.find('S'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('a'))
print(name.replace('S', 's'))
print(name*3)


# type casting
x = 1
y = 2.0
z = '3'

# x = float(x)
# y = float(y)
# z = float(z)

print('X is ' + str(x))
print('Y is ' + str(y))
print(z*3)

print('___________________')


# INPUT

# name = input('What is your name?: ')
# age = int(input('How old are you?: '))
# height = float(input('How tall are you?: '))
#
# age = age + 1
# print("Hello " + name)
# print("You are " + str(age) + ' years old')
# print('You are ' + str(height) + 'cm tall')

print('___________________')


import math


pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(pi))

x = 1
y = 2
z = 3

print(max(x, y, z))
print(min(x, y, z))

# slicing   - indexing[] and slice() [start, stop, step]



