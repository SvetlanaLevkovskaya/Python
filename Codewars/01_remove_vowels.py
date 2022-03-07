string_ = "This website is for losers LOL!"
string_new = []
for letter in string_:
    if letter.lower() not in "aeiou":
        string_new.append(letter)
print(''.join(string_new))


def disemvowel(string):
    return "".join(letter for letter in string if letter.lower() not in "aeiou")


print(disemvowel("This website is for losers LOL!"))


def shortcut(s):
    return s.translate(None, 'aeiou')


print(disemvowel("This website is for losers LOL!"))


def fake_bin(x):
    return ''. join('0' if int(i) < 5 else '1' for i in x)


print(fake_bin("45385593107843568"))
