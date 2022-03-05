def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"


def hello(name=""):
    return f"Hello, {name.capitalize() if name else 'World'}!"

def hello(name=''):
    return 'Hello, World!' if not name  else f'Hello, {name.capitalize()}!'