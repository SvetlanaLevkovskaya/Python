def is_digit(n):
    return n.isdigit() and len(n) == 1


print(is_digit(""))
print(is_digit("2"))
print(is_digit("a2"))
print(is_digit("222"))
