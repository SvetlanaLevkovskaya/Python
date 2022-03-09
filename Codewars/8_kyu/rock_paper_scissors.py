def rps(p1, p2):
    a = ['rockscissors', 'scissorspaper', 'paperrock']
    if p1 == p2:
        return "Draw!"
    return 'Player {} won!'.format(1 if p1 + p2 in a else 2)


print(rps('rock', 'paper'))


def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


print(rps('rock', 'scissors'))
