"""name_shuffler('john McClane'); => "McClane john"""

def name_shuffler(str_):
    s = str_.split()
    return ''.join('{} {}'.format(s[1], s[0]))


print(name_shuffler('john McClane'))


def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


print(name_shuffler('john McClane'))



