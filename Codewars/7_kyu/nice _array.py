def is_nice(arr):
    s = set(arr)
    return bool(arr) and all( n+1 in s or n-1 in s for n in s)


print(is_nice([2, 10, 9, 3]))
print(is_nice([3, 4, 5, 7]))


def is_nice(arr):
    return all(x+1 in arr or x-1 in arr for x in arr) and len(arr) > 0


print(is_nice([2, 10, 9, 3]))
print(is_nice([3, 4, 5, 7]))


def is_nice(arr):
    for x in arr:
        if x + 1 not in arr and x - 1 not in arr:
            return False
    return True and len(arr) > 0


print(is_nice([2, 10, 9, 3]))
print(is_nice([3, 4, 5, 7]))
