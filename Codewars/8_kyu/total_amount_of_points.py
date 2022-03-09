

def points(games):
    count = 0
    for x in games:
        if x[0] > x[2]:
            count += 3
        elif x[0] == x[2]:
            count += 1
    return count


print(points(['1:0','2:0','3:0','4:4','2:1','3:1','4:1','3:2','1:2','4:3']))


def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


print(points(['1:0','2:0','3:0','4:4','2:1','3:1','4:1','3:2','1:2','4:3']))


points = ['1:0','2:0','3:0','4:4','2:1','3:1','4:1','3:2','1:2','4:3']
count = 0
for x in points:
    if x[0] > x[2]:
        count += 3
    elif x[0] == x[2]:
        count += 1
print(count)
