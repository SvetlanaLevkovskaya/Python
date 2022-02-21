"""Jenny has written a function that returns a greeting for a user. However,
she's in love with Johnny, and would like to greet him slightly different."""


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


print(greet('Johnny'))
