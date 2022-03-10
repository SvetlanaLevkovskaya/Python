def include(arr,item):
    if item in arr:
        return True
    return False


print(include([1,2,3,4], 3))


def include(arr,item):
    return item in arr


print(include([1,2,3,4], 3))
