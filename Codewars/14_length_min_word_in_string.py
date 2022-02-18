def find_short(s):
    # l = min(s.split(" "), key=len)
    return len(min(s.split(" "), key=len)) # l: shortest word length


print(find_short("bitcoin take over the world maybe who knows perhaps"))


def find_short(s):
    return min(len(x) for x in s.split())


print(find_short("bitcoin take over the world maybe who knows perhaps"))
