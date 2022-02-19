def greet(name):
    return f"Hello, {name} how are you doing today?"


print(greet('Svetlana'))


def greet(name):
    return "Hello, {} how are you doing today?".format(name)


print(greet('Svetlana'))