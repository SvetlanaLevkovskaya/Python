def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))


print(get_number_from_string('jhgh52kjh1'))


def get_number_from_string(string):
    return [x for x in string if x.isdigit()]


print(get_number_from_string('jhgh52kjh1'))
