""""3 needs to become $3.00
3.1 needs to become $3.10"""


def format_money(amount):
    return "${:.2f}".format(amount)


print(format_money(39.99))
print(format_money(3))
