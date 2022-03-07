def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        winner = teams[0] + ' won!'
    elif scores[0] < scores[1]:
        winner = teams[1] + ' won!'
    else:
        winner = 'teams played draw.'

    return 'At match ' + teams[0] + ' - ' + teams[1] + ', ' + winner


print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))


def uefa_euro_2016(teams, scores):
    return f"At match {teams[0]} - {teams[1]}, " \
           f"{'teams played draw.' if scores[0] == scores[1] else teams[scores.index(max(scores))] + ' won!'}"


print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))
