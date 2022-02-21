"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
patrick feeney => P.F"""


def abbrev_name(name):
    n = name.split()
    return "{}.{}".format(n[0][0], n[1][0]).upper()


print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))


def abbrev_name(name):
    return '.'.join(w[0] for w in name.split()).upper()


print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))


def abbrev_name(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]


print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))



