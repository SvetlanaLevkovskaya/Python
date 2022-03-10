"""Create a method partition that accepts a list and a method/block. It should return two arrays: the first,
with all the elements for which the given block returned true, and the second for the remaining elements."""


def partition(arr, classifier_method):
    b = []
    x = list(filter(classifier_method, arr))
    for i in arr:
        if i not in x:
            b.append(i)
    return x, b


print(partition(['cat', 'dog', 'cow'], ['duck', 'donkey']))


def partition(list, m):
    return ([x for x in list if m(x)],[x for x in list if not m(x)])


print(partition(['cat', 'dog', 'cow'], ['duck', 'donkey']))
