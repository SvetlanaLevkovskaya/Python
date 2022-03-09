def remove(s, n):
    return s.replace("!", "", n)


print(remove("!!!Hi !!hi!!! !hi", 100))
print(remove("!!!Hi !!hi!!! !hi", 5))
print(remove("!!!Hi", 3))


def remove(s, n):
    l = []
    k = 1
    for i in range(len(s)):
        if s[i] == "!" and k <= n:
            k += 1
        else:
            l.append(s[i])
    return "".join(l)


print(remove("!!!Hi !!hi!!! !hi", 100))
print(remove("!!!Hi !!hi!!! !hi", 5))
print(remove("!!!Hi", 3))
