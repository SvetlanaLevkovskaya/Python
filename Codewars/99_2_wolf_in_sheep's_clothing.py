"""If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return
"Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue."""


def warn_the_sheep(queue):
    queue.reverse()
    wolf_position = queue.index('wolf')
    if wolf_position == 0:
        return "Pls go away and stop eating my sheep"
    return f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!"


print(warn_the_sheep(['sheep', 'sheep', 'wolf']))
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))


def warn_the_sheep(queue):
    i = queue[::-1].index('wolf')
    if i == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'


print(warn_the_sheep(['sheep', 'sheep', 'wolf']))
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
