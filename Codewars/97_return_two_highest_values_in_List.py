import heapq


def two_highest(arg1):
    return heapq.nlargest(2, set(arg1))


print(two_highest([15, 20, 20, 17]))
print(two_highest([]))
print(two_highest([1, 1, 1, 1]))


def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]


print(two_highest([15, 20, 20, 17]))
print(two_highest([]))
print(two_highest([1, 1, 1, 1]))
