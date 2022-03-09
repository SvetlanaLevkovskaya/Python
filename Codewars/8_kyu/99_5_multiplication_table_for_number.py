def multi_table(number):
    for i in range(1, 11):
        print(str(i) + ' * ' + str(number) + ' = ' + str(i*number))


multi_table(5)


def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


print(multi_table(5))


def multi_table(number):
    table = ["{} * {} = {}".format(i, number, i * number) for i in range(1, 11)]
    return '\n'.join(table)


print(multi_table(5))
