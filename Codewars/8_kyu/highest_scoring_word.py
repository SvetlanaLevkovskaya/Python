def highest_scoring_word(words):
    return max(words.split(), key=lambda word: sum(map(ord, word)) - 96*len(word))


print(highest_scoring_word("The sunset sets at twelve o' clock."))


def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high("The sunset sets at twelve o' clock."))

def high(x):
    words=x.split()
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


print(high("The sunset sets at twelve o' clock."))


def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c) - 96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word

    return highest_word


print(high("The sunset sets at twelve o' clock."))
