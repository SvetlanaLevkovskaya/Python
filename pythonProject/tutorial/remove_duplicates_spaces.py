s = input('Enter a string: ')
s_new = 'new string = '

for x in s:
    if x not in s_new and x != ' ':
        s_new += x
print(s_new)
