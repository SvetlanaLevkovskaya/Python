def validate_code(code):
    return str(code).startswith(('1', '2', '3'))


print(validate_code(123))


def validate_code(code):
    return str(code).startswith(('1', '2', '3'))


print(validate_code(123))


def validate_code(code):
    return str(code)[0] in '123'


print(validate_code(123))


def validate_code(code):
    import re
    return bool(re.match(r"^[123]\d*$", str(code)))


print(validate_code(123))
