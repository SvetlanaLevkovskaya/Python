# lists: ordered, immutable, text representation

my_string = "Hello, world"
print(my_string)

print('*'*80)
my_string = 'I\'m a programmer'
print(my_string)

print('*'*80)
my_string = "I'm a programmer"
print(my_string)

print('*'*80)
my_string = """I'm a 
programmer"""
print(my_string)

print('*'*80)
my_string = """I'm a \
programmer"""
print(my_string)

print('*'*80)
my_string = "Hello, world"
char = my_string[0]
print('char = my_string[0]', '                        ', char)

print('*'*80)
my_string = "Hello, world"
print('my_string', '                                  ', my_string)
substring = my_string[1:5]
print('substring = my_string[1:5]', '                 ', substring)
substring = my_string[:]
print('substring = my_string[:]', '                   ', substring)
substring = my_string[::2]
print('substring = my_string[::2]', '                 ', substring)
substring = my_string[::-1]
print('substring = my_string[::-1]', '                ', substring)

print('*'*80)
greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name
print('sentence = greeting + ' ' + name', '              ', sentence)

print('*'*80)
greeting = "hello"
for x in greeting:
    print(x)

if "e" in greeting:
    print("yes")

print('*'*80)
my_string = "    Hello world   "
print('my_string = "    Hello world   "', '              ', my_string)
my_string = my_string.strip()
print('my_string = my_string.strip()', '                 ', my_string)
my_string = "    Hello world   "
my_string.strip()
print('my_string.strip()', '                             ', my_string) # immutable!!!

print('*'*80)
my_string = "Hello world"
print("my_string = 'Hello world'", '                     ', my_string)
print('my_string.upper()', '                             ', my_string.upper())
print('my_string.lower()', '                             ', my_string.lower())
print('my_string.startswith("H")', '                     ', my_string.startswith('Hello'))
print('my_string.endswith("d")', '                       ', my_string.endswith('world'))
print('my_string.find("o")', '                           ', my_string.find('o'))
print('my_string.find("lo")', '                          ', my_string.find('lo'))
print('my_string.find("p")', '                           ', my_string.find('p'))
print('my_string.count("o")', '                          ', my_string.count('o'))
print('my_string.replace("world", "universe)', '         ', my_string.replace("world", "universe"))
print('my_string', '                                     ', my_string)
print('my_string.replace("worrrrld", "universe)', '      ', my_string.replace("worrrld", "universe"))
print('my_string', '                                     ', my_string)

print('*'*80)
my_string = "how are you doing"
my_list = my_string.split()
print("my_list = my_string.split()", '                   ', my_list)
print("my_list = my_string.split()", '                   ', type(my_list))

print('*'*80)
my_string = "how,are,you,doing"
my_list = my_string.split(",")
print("my_list = my_string.split(',')", '                 ', my_list)

print('*'*80)
my_string = "how,are,you,doing"
my_list = my_string.split(",")
print("my_list = my_string.split(',')", '                 ', my_list)
new_string = ''.join(my_list)
print("''.join(my_list)", '                                ', new_string)
new_string = ' '.join(my_list)
print("' '.join(my_list)", '                               ', new_string)

print('*'*80)
my_list = ['a'] * 6
print("my_list = ['a'] * 6", '                             ', my_list)



from timeit import default_timer as timer

# bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print('for i in my_list:my_string += i', '                 ', my_string)
print("stop - start", "                                    ", stop - start)

# good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print("my_string = ''.join(my_list)", '                    ', my_string)
print("stop - start", "                                    ", stop - start)

print('*'*80)
my_list = ['a'] * 1000000
# bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print("stop - start", "                                    ", stop - start)

# good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print("stop - start", "                                    ", stop - start)

print('*'*80)
# %, .format(), f-Strings
var = 'Tom'
print("var", "                                              ", var)
my_string = 'the variable is %s' %var
print("'the variable is %s' %var", '                        ', my_string)

print('*'*80)
var = 3
print("var", "                                              ", var)
my_string = 'the variable is %d' %var
print("'the variable is %d' %var", '                        ', my_string)

print('*'*80)
var = 3.56558888
print("var", "                                              ", var)
my_string = 'the variable is %f' %var
print("'the variable is %f' %var", '                        ', my_string)

print('*'*80)
var = 3.56558888
print("var", "                                              ", var)
my_string = 'the variable is %.2f' %var
print("'the variable is %f' %var", '                        ', my_string)

print('*'*80)
var = 3.56558888
print("var", "                                              ", var)
my_string = 'the variable is {}'.format(var)
print("'the variable is {}'.format(var)", '                 ', my_string)

print('*'*80)
var = 3.56558888
print("var", "                                              ", var)
my_string = 'the variable is {:.2f}'.format(var)
print("'the variable is {:.2}'.format(var)", '              ', my_string)

print('*'*80)
var = 3.56558888
var2 = 6
print("var", "                                              ", var, var2)
my_string = 'the variable is {:.2f} and {}'.format(var, var2)
print("'the variable is {:.2} and {}'.format(var,var2)", '  ', my_string)


print('*'*80)
var = 3.56558888
var2 = 6
print("var", "                                              ", var, var2)
my_string = f'the variable is {var} and {var2}'
print('f"the variable is {var} and {var2}"', '              ', my_string)

print('*'*80)
var = 3.56558888
var2 = 6
print("var", "                                              ", var, var2)
my_string = f'the variable is {var*2} and {var2}'
print('f"the variable is {var*2} and {var2}"', '            ', my_string)

