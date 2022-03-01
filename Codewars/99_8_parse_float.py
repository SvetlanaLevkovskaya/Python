"""Write function parse_float which takes a string/list
and returns a number or 'none' if conversion is not possible."""


def parse_float(string):
    try:
        return float(string)
    except:
        return None


print(parse_float("234.0234"))
print(parse_float("a"))
