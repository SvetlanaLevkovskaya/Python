# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"
#
# print(dir(Person))
import datetime

print(dir())

print(hex(10), type(hex(10)))

# help('modules')

now = datetime.datetime.today()
print(now)

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print((type(moon_landing_datetime)))


# 1
print(len("95637+12"))
# 2
score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")
# 3
# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
#
#
# a_function(10)
# print(a_parameter)

# 4
def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

# 5
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)

# 6
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
