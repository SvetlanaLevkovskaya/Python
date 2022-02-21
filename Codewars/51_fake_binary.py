"""Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string."""


def fake_bin(x):
    return ''.join('0' if int(a) < 5 else '1' for a in x)


print(fake_bin("45385593107843568"))


def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

print(fake_bin("45385593107843568"))


def fake_bin(x):
    a_x = ""
    for a in x:
        if a < '5':
            a_x += "0"
        else:
            a_x += "1"
    return a_x


print(fake_bin("45385593107843568"))
