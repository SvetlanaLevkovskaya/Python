""" each lowercase letter becomes uppercase and each uppercase letter becomes lowercase."""


def to_alternating_case(string):
    return string.swapcase()


print(to_alternating_case("ALTerNAtiNG CaSe"))


def to_alternating_case(string):
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])


print(to_alternating_case("ALTerNAtiNG CaSe"))
