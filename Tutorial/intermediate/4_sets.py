# sets: unordered, mutable, no duplicates

myset = {}
print('myset = {}', '                                  ', myset)
print(type(myset))

print('*'*80)
myset = set()
print('myset = set()', '                               ', myset)
print(type(myset))

print('*'*80)
myset = {1, 3, 4}
print('myset = {1, 3, 4}', '                           ', myset)
print(type(myset))

myset = {1, 3, 4, 1, 3}
print('myset = {1, 3, 4, 1, 3}', '                     ', myset)
print(type(myset))

print('*'*80)
myset = set([1,2,3])
print('myset = set([1,2,3])', '                        ', myset)
print(type(myset))

print('*'*80)
myset = set("Hello")
print('myset = set("Hello")', '                        ', myset)
print(type(myset))

print('*'*80)
myset = set()
print('myset = set()', '                               ', myset)
myset.add(1)
print('myset.add(1)', '                                ', myset)
myset.add(2)
print('myset.add(2)', '                                ', myset)
myset.add(3)
print('myset.add(3)', '                                ', myset)

print('*'*80)
print('myset', '                                       ', myset)
myset.remove(3)
print('myset.remove(3)', '                             ', myset)


print('*'*80)
myset = {1, 2, 3}
print('myset', '                                       ', myset)
myset.pop()
print('myset.pop()', '                                 ', myset)


print('*'*80)
print('myset = set()', '                               ', myset)
myset.discard(2)
print('myset.discard(2)', '                            ', myset)


print('*'*80)
print('myset', '                                       ', myset)
myset.clear()
print('myset.clear()', '                              ', myset)

print('*'*80)
myset = {1, 2, 3}
print('myset', '                                       ', myset)
for i in myset:
    print(i)

if 1 in myset:
    print("yes")

print('*'*80)
odds = {1, 3, 5, 7, 9}
print('odds', '                                         ', odds)
evens = {0, 2, 4, 6, 8}
print('evens', '                                        ', evens)
primes = {2, 3, 5, 7}
print('primes', '                                       ', primes)

u = odds.union(evens)
print('odds.union(evens)', '                            ', u)

i = odds.intersection(evens)
print('odds.intersection(evens)', '                     ', i)

i = odds.intersection(primes)
print('odds.intersection(primes)', '                    ', i)

i = evens.intersection(primes)
print('evens.intersection(primes)', '                   ', i)

print('*'*80)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('setA', '                                         ', setA)
setB = {1, 2, 3, 10, 11, 12}
print('setB', '                                         ', setB)

diff = setA.difference(setB)
print('setA.difference(setB)', '                        ', diff)

diff = setB.difference(setA)
print('setB.difference(setA)', '                        ', diff)

print('*'*80)
diff = setA.symmetric_difference(setB)
print('setA.symmetric_difference(setB)', '              ', diff)

diff = setB.symmetric_difference(setA)
print('setB.symmetric_difference(setA)', '              ', diff)

print('*'*80)
print('setA', '                                         ', setA)
print('setB', '                                         ', setB)
setA.update(setB)
print('setA.update(setB)', '                            ', setA)

print('*'*80)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('setA', '                                         ', setA)
setB = {1, 2, 3, 10, 11, 12}
print('setB', '                                         ', setB)
setA.intersection_update(setB)
print('setA.intersection_update(setB)', '               ', setA)


print('*'*80)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('setA', '                                         ', setA)
setB = {1, 2, 3, 10, 11, 12}
print('setB', '                                         ', setB)
setA.difference_update(setB)
print('setA.difference_update(setB)', '                 ', setA)


print('*'*80)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('setA', '                                         ', setA)
setB = {1, 2, 3, 10, 11, 12}
print('setB', '                                         ', setB)
setA.symmetric_difference_update(setB)
print('setA.symmetric_difference_update(setB)', '       ', setA)

print('*'*80)
setA = {1, 2, 3, 4, 5, 6}
print('setA', '                                         ', setA)
setB = {1, 2, 3}
print('setB', '                                         ', setB)
print('setA.issubset(setB)', '                          ', setA.issubset(setB))
print('setB.issubset(setA)', '                          ', setB.issubset(setA))
print('setA.issuperset(setB)', '                        ', setA.issuperset(setB))
print('setB.issuperset(setA)', '                        ', setB.issuperset(setA))
print('setA.isdisjoint(setB)', '                        ', setA.isdisjoint(setB))
print('setB.isdisjoint(setA)', '                        ', setB.isdisjoint(setA))
setC = {7, 8}
print('setC', '                                         ', setC)
print('setA.isdisjoint(setC)', '                        ', setA.isdisjoint(setC))

print('*'*80)
setA = {1, 2, 3, 4, 5, 6}
print('setA', '                                         ', setA)
setB = setA
print('setB', '                                         ', setB)
setB.add(7)
print('setA, setB.add(7)', '                            ', setA)
print('setB, setB.add(7)', '                            ', setB)


print('*'*80)
setA = {1, 2, 3, 4, 5, 6}
print('setA', '                                         ', setA)
setB = setA.copy()
print('setB', '                                         ', setB)
setB.add(7)
print('setA, setB.add(7)', '                            ', setA)
print('setB, setB.add(7)', '                            ', setB)

print('*'*80)
setA = {1, 2, 3, 4, 5, 6}
print('setA', '                                         ', setA)
setB = set(setA)
print('setB', '                                         ', setB)
setB.add(7)
print('setA, setB.add(7)', '                            ', setA)
print('setB, setB.add(7)', '                            ', setB)

print('*'*80)
a = frozenset([1, 2, 3, 4])
print('frozenset([1, 2, 3, 4])', '                       ', a)
print('frozenset([1, 2, 3, 4])', '                       ', type(a))
