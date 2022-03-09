def problem(a):
    return "Error" if isinstance(a, str) else a*50 + 6


print(problem("hello"))
print(problem(56))


def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"


print(problem("hello"))
print(problem(56))
