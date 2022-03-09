def filter_list(l):
    new_list = []
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list


print(filter_list([1, 2, 'aasf', '1', '123', 123]))


def filter_list(l):
    return [x for x in l if type(x) != str]


print(filter_list([1, 2, 'aasf', '1', '123', 123]))


def filter_list(l):
    return [x for x in l if not isinstance(x, str)]


print(filter_list([1, 2, 'aasf', '1', '123', 123]))


# def filter_list(l):
#   return [x for x in l if isinstance(x, int)]
#
#
# print(filter_list([1, 0.2, 'aasf', '1', '123', 123]))
