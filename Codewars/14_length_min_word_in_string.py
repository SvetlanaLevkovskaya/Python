def find_short(s):
    return len(min(s.split(" "), key=len))


print(find_short("bitcoin take over the world maybe who knows perhaps"))


def find_short(s):
    return min(len(x) for x in s.split())


print(find_short("bitcoin take over the world maybe who knows perhaps"))
