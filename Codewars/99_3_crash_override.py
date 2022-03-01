FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}


def alias_gen(f_name, l_name):
    first = FIRST_NAME.get(f_name[0].upper())
    last = SURNAME.get(l_name[0].upper())
    return '{} {}'.format(first, last) if first and last else \
        'Your name must start with a letter from A - Z.'


def alias_gen(f_name, l_name):
    try:
        return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
    except:
        return 'Your name must start with a letter from A - Z.'


