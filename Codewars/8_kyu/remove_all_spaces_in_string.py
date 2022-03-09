def no_space(x):
    return x.replace(" ", "")


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))


def no_space(x):
    return "".join(x.split())

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
