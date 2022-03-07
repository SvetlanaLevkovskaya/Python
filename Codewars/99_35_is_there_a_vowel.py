def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]


# print(is_vow([118,"u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106]))
print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]))


def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]


print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]))
