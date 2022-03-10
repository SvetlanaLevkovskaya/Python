# tuple - кортеж - не изменяемый список

# tuple = ('first', 25, 25.1,)
# print(tuple)

# tuple = ('first',)
# print(type(tuple))
#
# tuple = ('first')
# print(type(tuple))

# print(tuple([1,4,6,9,5,2]))
# print(list((1,3,5,6,9,)))

dict = {'name': 'Svetlana', 'age': 42, 'salary': 5000}
print(dict)
for k in dict.keys():
    print('k = ', k)

print('+++++++++++++++++++++++++++++++++++')

for v in dict.values():
    print('v =', v)
print('+++++++++++++++++++++++++++++++++++')

for i in dict.items():
    print('i =', i)

print('+++++++++++++++++++++++++++++++++++')

print(dict['salary'])

print('+++++++++++++++++++++++++++++++++++')
dict['salary'] = 10000
print(dict)

print('+++++++++++++++++++++++++++++++++++')
del(dict['salary'])
print(dict)
