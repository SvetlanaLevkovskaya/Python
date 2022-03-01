def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')


print(chromosome_check('XX'))


def chromosome_check(sperm):
    gender = {"XY": "son", "XX": "daughter"}

    return "Congratulations! You're going to have a {}.".format(gender[sperm])


print(chromosome_check('XX'))


def chromosome_check(sperm):
    return "Congratulations! You\'re going to have a daughter." if sperm == 'XX' \
        else "Congratulations! You\'re going to have a son."


print(chromosome_check('XX'))
