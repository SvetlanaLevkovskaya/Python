# 1.
# x = int(input("Enter a x: "))
# y = int(input("Enter a y: "))
#
#
# def sum(x, y):
#     return x + y
#
#
# z = sum(x,y)
# print(z)


#2.
# def sum(x, y):
#     return x + y
# print(sum(10, 20))

# 3.
# def f(a=2):
#     return 2*a - 2
#
#
# print(f(4))

# # 4.
# a = 45
# b = 5
# def f(a, b):
#     print(a)
#     print(b)
#
# f(a,b)

# 5.
a = 45
b = 5
def f():
    global a
    a = a + 2
    print(a)


f()
print(a)
