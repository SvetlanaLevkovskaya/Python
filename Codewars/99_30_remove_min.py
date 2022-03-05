def remove_smallest(numbers):
    if len(numbers) <= 1:
        return []
    numbers.remove(min(numbers))
    return numbers


print(remove_smallest([5, 3, 2, 1, 4]))


def remove_smallest(numbers):
    if len(numbers) < 1 :
        print(numbers)
    else:
        numbers.remove(min(numbers))
        print(numbers)


remove_smallest([1, 2, 3, 1, 1])


def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


print(remove_smallest([5, 3, 2, 1, 4]))
