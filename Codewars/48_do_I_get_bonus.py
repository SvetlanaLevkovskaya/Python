def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))


print(bonus_time(100000, True))
print(bonus_time(100000, False))
