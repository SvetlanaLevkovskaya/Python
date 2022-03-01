"""you need a method, which returns the smallest unused ID for your next new data item...
Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs,
but you don't have to find or remove them!"""


def next_id(arr):
    t = 0
    while t in arr:
        t += 1
    return t


print(next_id([17, 19, 9, 12, 17, 2, 16, 1, 10, 9, 20, 10, 20, 8, 17, 0, 1, 9, 20, 19, 0, 13, 20, 5, 18, 8]))
print(next_id([0,1,2,3,4,5,6,7,8,9,10]))


def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i


print(next_id([17, 19, 9, 12, 17, 2, 16, 1, 10, 9, 20, 10, 20, 8, 17, 0, 1, 9, 20, 19, 0, 13, 20, 5, 18, 8]))
print(next_id([0,1,2,3,4,5,6,7,8,9,10]))
