def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join([x for x in s if x not in '0123456789'])


print(string_clean("123456789"))
print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"))


def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())


print(string_clean("123456789"))
print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"))
