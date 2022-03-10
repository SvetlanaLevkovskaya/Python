import re


def validate_usr(username):
    return re.match('^[a-z0-9_]{4,16}$', username) != None


print(validate_usr('asddsa'))


def validate_usr(username):
    return bool(re.match('^[a-z0-9_]{4,16}$', username))


print(validate_usr('asddsa'))


def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False
    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    for i in username:
        if i not in allowed:
            return False
    return True


print(validate_usr('asddsa'))
