# dictionaries: key_value pairs, unordered, mutable

mydict = {}
print(mydict)

mydict = {"name": "Max", "age": 27, "city": "Boston"}
print(mydict)

mydict2 = dict(name="Max",age=27, city="Boston")
print(mydict2)

print('*'*80)

value = mydict["name"]
print('value = mydict["name"]', '                 ', value)

print('*'*80)
mydict["email"] = "123@gmail.com"
print('mydict["email"] = "123@gmail.com"', '      ', mydict)

mydict["email"] = "4@gmail.com"
print('mydict["email"] = "4@gmail.com"', '        ', mydict)

print('*'*80)
print('mydict = ', '                              ', mydict)
del mydict["name"]
print('del mydict["name"] = ', '                  ', mydict)

mydict.pop("age")
print('mydict.pop("age") = ', '                   ', mydict)

mydict.popitem()
print('mydict.popitem() = ', '                    ', mydict)

print('*'*80)
if "name" in mydict2:
    print(mydict2["name"])

try:
    print(mydict2["lastname"])
except:
    print("Error")

print('*'*80)
for key in mydict2:
    print('key = ', '               ', key)

print('*'*80)
for key in mydict2.keys():
    print('key = ', '               ', key)

print('*'*80)
for value in mydict2.values():
    print('value = ', '             ', value)

print('*'*80)
for key, value in mydict2.items():
    print('key, value = ', '        ', key, value)

print('*'*80)
mydict2_cpy = mydict2
print('mydict2_cpy = mydict2', '                        ', mydict2)
print('mydict2_cpy = mydict2', '                        ', mydict2_cpy)
mydict2_cpy["email"] = "123@gmail.com"
print('mydict2_cpy["email"] = "123@gmail.com"', '       ', mydict2_cpy)
print('mydict2_cpy["email"] = "123@gmail.com"', '       ', mydict2)
del mydict2["email"]

print('*'*80)
mydict2_cpy = mydict2.copy()
print('mydict2_cpy = mydict2.copy()', '                 ', mydict2)
print('mydict2_cpy = mydict2.copy()', '                 ', mydict2_cpy)
mydict2_cpy["email"] = "4@gmail.com"
print('mydict2_cpy["email"] = "4@gmail.com"', '         ', mydict2_cpy)
print('mydict2_cpy["email"] = "4@gmail.com"', '         ', mydict2)


print('*'*80)
mydict2_cpy = dict(mydict2)
print('mydict2_cpy = dict(mydict2)', '                  ', mydict2)
print('mydict2_cpy = dict(mydict2)', '                  ', mydict2_cpy)
mydict2_cpy["email"] = "4@gmail.com"
print('mydict2_cpy["email"] = "4@gmail.com"', '         ', mydict2_cpy)
print('mydict2_cpy["email"] = "4@gmail.com"', '         ', mydict2)


print('*'*80)
my_dict = {"name": "Max", "age": 28, "email": "4@gmail.com"}
print('my_dict', '                                      ', my_dict)

my_dict_2 = dict(name="Mary", age=27, city="Boston")
print('my_dict_2', '                                    ', my_dict_2)

my_dict.update(my_dict_2)
print('my_dict.update(my_dict_2)', '                    ', my_dict)

print('*'*80)
my_dict = {3: 9, 6: 36, 9: 81}
print('my_dict', '                                      ', my_dict)
value = my_dict[3]
print('value = my_dict[3]', '                           ', value)

print('*'*80)
mytyple = (8, 7)
mydict = {mytyple: 15}
print('mydict = {mytyple: 15} ', '                        ', mydict)

print('*'*80)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', '40']))
print("dict(zip(['name', 'job', 'age'], ['Bob', 'dev', '40']))", '    ', bob2)

print(1/5)
print(1//5)
print(1%5)
print(0.1+0.1+0.1-0.3)
print(round(0.1+0.1+0.1-0.3))
print(set('spam'))
print("s\tp\na\0m")
print("Meaning " ,"of" ," life")
