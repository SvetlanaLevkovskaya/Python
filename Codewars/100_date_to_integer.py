import datetime
from datetime import date


def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length


first_date = date(2020, 10, 2)
second_date = date(2020, 10, 30)
delta = second_date - first_date
print(delta)


a = datetime.datetime.now()
b = datetime.date.today()
x = date(2022, 1, 21)
print(type(x))
print(datetime.timedelta())

