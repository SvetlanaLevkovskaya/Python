def lowercase_count(strng):
    return sum(a.islower() for a in strng)


print(lowercase_count("abcABC123"))
