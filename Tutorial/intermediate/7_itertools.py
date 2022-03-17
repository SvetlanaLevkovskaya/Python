# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print('a', '                                          ', a)
print('b', '                                          ', b)
print('list(product(a, b)', '                         ', list(prod))
prod = product(a, b, repeat=2)
print('list(product(a, b, repeat=2)', '               ', list(prod))

print("*"*80)
from itertools import permutations
a = [1, 2, 3]
b = [3, 4]
perm = permutations(a)
print('a', '                                          ', a)
print('list(permutations(a))', '                      ', list(perm))
perm = permutations(a, 2)
print('list(permutations(a, 2))', '                   ', list(perm))

print("*"*80)
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3]
comb = combinations(a, 2)
print('a', '                                          ', a)
print('list(combinations(a, 2))', '                   ', list(comb))
comb_wr = combinations_with_replacement(a, 2)
print('combinations_with_replacement(a, 2)', '        ', list(comb_wr))

print("*"*80)
from itertools import accumulate
import operator
a = [1, 2, 3]
acc = accumulate(a)
print('a', '                                          ', a)
print('list(accumulate(a))', '                        ', list(acc))
a = [1, 2, 3, 4]
print('a', '                                          ', a)
acc_mul = accumulate(a, func=operator.mul)
print('list(accumulate(a, func=operator.mul))', '     ', list(acc_mul))
a = [1, 2, 5, 3, 4]
print('a', '                                          ', a)
acc_max = accumulate(a, func=max)
print('list(accumulate(a, func=max))', '              ', list(acc_max))

print("*"*80)
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print('a', '                                          ', a)
print('groupby(a, key=smaller_than_3)', '             ', group_obj)
# print('[key for key in group_obj]', '                 ', [key for key in group_obj])
for key, value in group_obj:
    print('key, list(value)', '                           ', key, list(value))

print("*"*80)
b = [1, 2, 3, 4]
group_obj = groupby(b, key=lambda x: x < 3)
print('b', '                                          ', b)
print('groupby(b, key=lambda x: x < 3)', '            ', group_obj)
for key, value in group_obj:
    print('key, list(value)', '                           ', key, list(value))


print("*"*80)
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Clare', 'age': 28}]

print('persons', '                                    ', persons)
group_obj = groupby(persons, key=lambda x: x['age'])
print('groupby(persons, key=lambda x: x["age"])', '   ', group_obj)
for key, value in group_obj:
    print('key, list(value)', '                           ', key, list(value))

print("*"*80)
from itertools import count, cycle, repeat

for i in count(10):
    print('for i in count(10)', '          ', i)
    if i == 15:
        break

print("*"*80)
a = [1, 2, 3]
for i in cycle(a):
    print('for i in cycle(1, 2, 3])', '     ', i)
    if i == 3:
        break

print("*"*80)
a = [1, 2, 3]
for i in repeat(1, 4):
    print('for i in repeat(1, 4)', '  ', i)
    if i == 3:
        break
