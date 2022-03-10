def update_light(current):
    lights = ['green', 'yellow', 'red']
    return lights[(lights.index(current)+1) % len(lights)]


print(update_light('green'))
print(update_light('red'))


def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

print(update_light('green'))
print(update_light('red'))


lights = ['green', 'yellow', 'red']

print(len(lights))
