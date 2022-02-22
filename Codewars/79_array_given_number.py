def how_much_i_love_you(nb_petals):
    x = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    return x[(nb_petals-1) % len(x)]


print(how_much_i_love_you(107))


def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]


print(how_much_i_love_you(107))
