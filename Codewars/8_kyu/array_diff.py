# def array_diff(a, b):
    # return 'a was ' + str(a) + ', ' + 'b was ' + str(b) + ', ' +'expected '+ str(list(set(a) - set(b)))
    # return f"a was str {str(a)}, b was {str(b)}, expected {str(list(set(a) - set(b)))}"


def array_diff(a, b):
    return [x for x in a if x not in b]


def array_diff(a, b):
    return [x for x in a if x not in set(b)]


a = [1, 2, 2]
b = [1]
print(list(set(a) - set(b)))
print(array_diff([1, 2, 2], [1]))
