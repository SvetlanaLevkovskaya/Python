def who_is_paying(name):
    if len(name) > 2:
        return [name, name[0:2]]
    return [name]


print(who_is_paying("Mexico"))
print(who_is_paying("Me"))
print(who_is_paying(""))


def who_is_paying(name):
    return [name,name[0:2]] if len(name)>2 else [name]


print(who_is_paying("Mexico"))
print(who_is_paying("Me"))
print(who_is_paying(""))
