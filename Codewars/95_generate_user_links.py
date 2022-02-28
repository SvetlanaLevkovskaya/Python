"""Your task is to create userlinks for the url, you will be given a username and must return a valid link."""


import urllib.parse


def generate_link(user):
    return 'http://www.codewars.com/users/' + urllib.parse.quote(user)


print(generate_link('matt c'))
