def shorten_to_date(long_date):
    l = long_date.replace(',', '')
    return ' '.join(l.split()[0:-1])


print(shorten_to_date("Monday February 2, 8pm"))


def shorten_to_date(long_date):
    return long_date.split(',')[0]


print(shorten_to_date("Monday February 2, 8pm"))


def shorten_to_date(long_date):
    date, time = long_date.split(",")
    return date


print(shorten_to_date("Monday February 2, 8pm"))
