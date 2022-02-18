def get_middle(s):
    middle = len(s) // 2
    if len(s) % 2 == 0:
        return s[middle - 1] + s[middle]
    return s[middle]


print(get_middle('aabzcc'))
print(get_middle('test'))
print(get_middle('testing'))
print(get_middle('a'))
