def contamination(text, char):
    return char*len(text)


print(contamination("abc", "z"))


def contamination(text, char):
    return "".join(char for x in text)


print(contamination("abc", "z"))
