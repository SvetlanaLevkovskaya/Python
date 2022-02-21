def find_average(numbers):
    return sum(x for x in numbers)/len(numbers)


print(find_average([1,2,3,4]))


def find_average(numbers):
    return sum(numbers)/len(numbers)


print(find_average([1,2,3,4]))


def find_average(array):
    return sum(array) / len(array) if array else 0


print(find_average([1,2,3,4]))

