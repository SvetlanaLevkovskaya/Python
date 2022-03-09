def say_hello(name, city, state):
    return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)


print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))
