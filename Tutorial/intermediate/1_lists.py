# lists: ordered, mutable, allows duplicate elements
mylist = []
print(mylist)
mylist = ["banana", "chery", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist[1]
print(item)

item = mylist[-1]
print(item)

print('*'*80)
for i in mylist:
    print(i)

print('*'*80)
if "banana" in mylist:
    print("yes")
print("no")


print('*'*80)
print('len() = ', '                       ', len(mylist))
print('mylist = ', '                      ', mylist)
mylist.append("lemon")
print('mylist.append("lemon") = ', '      ',  mylist)
mylist.insert(1, "blueberry")
print('mylist.insert(1, "blueberry") = ', mylist)
mylist.pop()
print('mylist.pop() = ', '                ', mylist)
mylist.remove("chery")
print('mylist.remove("chery") = ', '      ', mylist)
mylist.reverse()
print('mylist.reverse() = ', '            ', mylist)

print('*'*80)
new_list = sorted(mylist)                                  # create new sorted list
print('mylist = ', '                      ', mylist)
print('new_list.sorted(mylist) = ', '     ', new_list)
mylist.sort()                                              # sort existing list
print('mylist.sort() = ', '               ', mylist)

print('*'*80)
print('mylist * 2 = ', '                  ', mylist*2)
x = mylist + mylist2
print('mylist + mylist2 = ', '            ', x)

print('*' * 80)
a = x[0:2]
print('slicing [0:2] = ', '               ', a)
a = x[0:]
print('slicing [0:] = ', '                ', a)
a = x[::-1]
print('reverse list [::-1] = ', '         ', a)
a = x[:2]
print('slicing [:2] = ', '                ', a)
a = x[::2]
print('step=2 =  ', '                     ', a)

print('*'*80)
list_org = ["banana", "chery", "apple"]
list_cpy = list_org
print('list_cpy = ', '                    ', list_cpy)
list_cpy.append("lemon")
print('list_cpy = list_org', '            ', list_cpy)
print('list_org = ', '                    ', list_org)
list_cpy = list(list_org)
list_cpy.append("orange")
print('list_cpy = list(list_org)', '      ', list_cpy)
print('list_org = ', '                    ', list_org)
list_cpy = list_org[:]
list_cpy.append("mango")
print('list_cpy = list_org[:]', '         ', list_cpy)
print('list_org = ', '                    ', list_org)

print('*'*80)
a = [1, 2, 3, 4, 5, 6, 7]
b = [i*i for i in a]
print('a = ', '                           ', a)
print('a**2 = ', '                        ', b)

print('*'*80)
mylist.clear()
print('mylist.clear() = ', '              ', mylist)
