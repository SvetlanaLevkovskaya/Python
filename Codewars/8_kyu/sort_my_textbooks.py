def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)


print(sorter(['Algebra', 'history', 'Geometry', 'english']))


def sorter(textbooks):
    return sorted(textbooks, key=str.lower())


print(sorter(['Algebra', 'history', 'Geometry', 'english']))


ll = ['Algebra', 'history', 'Geometry', 'english']
ll.sort(key=str.lower)
print(ll)
