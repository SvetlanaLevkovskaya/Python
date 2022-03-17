# lambda arguments: expression
# map(func, seq)
# filter(func, seq)
# reduce(func, seq)

add10 = lambda x: x + 10
print('add10(5) = lambda x: x + 10', '                     ', add10(5))


def add10_func(x):
    return x + 10


mult = lambda x,y: x*y
print('mult(2,3) = lambda x,y: x*y', '                     ', mult(2, 3))

print('*'*80)
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print('points2D', '                                        ', points2D)
print('sorted(points2D)', '                                ', points2D_sorted)
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print('sorted(points2D, key=lambda x: x[1]', '             ', points2D_sorted)

print('*'*80)


def sort_by_y(x):
    return x[1]

print('points2D', '                                        ', points2D)
points2D_sorted = sorted(points2D, key=sort_by_y)
print('sorted(points2D, key=sort_by_y)', '                 ', points2D_sorted)

print('*'*80)
print('points2D', '                                        ', points2D)
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print('sorted(points2D, key=lambda x: x[0] + x[1]', '      ', points2D_sorted)

print('*'*80)
a = [1, 2, 3, 4, 5]
print('a', '                                                ', a)
b = map(lambda x: x*2, a)
print('list(map(lambda x: x*2, a))', '                      ', list(b))
c = [x*2 for x in a]
print('[x*2 for x in a]', '                                 ', c)

print('*'*80)
a = [1, 2, 3, 4, 5, 6]
print('a', '                                                ', a)
b = filter(lambda x: x % 2 == 0, a)
print('list(filter(lambda x: x % 2 == 0, a))', '            ', list(b))

print('*'*80)
a = [1, 2, 3, 4, 5, 6]
print('a', '                                                ', a)
c = [x for x in a if x % 2 == 0]
print('[x for x in a if x % 2 == 0]', '                     ', c)

from functools import reduce
print('*'*80)
a = [1, 2, 3, 4]
print('a', '                                                ', a)
product_a = reduce(lambda x, y: x*y, a)
print('reduce(lambda x, y: x*y, a)', '                      ', product_a)
