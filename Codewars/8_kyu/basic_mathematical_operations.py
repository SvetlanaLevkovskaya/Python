def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2


print(basic_op('+', 10, 5))


def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


print(basic_op('+', 10, 5))
