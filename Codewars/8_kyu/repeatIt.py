def repeat_it(string,n):
    return string * n if isinstance(string, str) else 'Not a string'


print(repeat_it('*', 3))


def repeat_it(string,n):
    if type(string) is not str:
        return 'Not a string'
    return string * n


print(repeat_it('*', 3))
