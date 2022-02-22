def correct_tail(body, tail):
    return body.endswith(tail)


print(correct_tail('Odhkbhzwalvmxphsvsxpwhjcetxd', 'm'))
print(correct_tail("Fox", "x"))
print(correct_tail("Meerkat", "t"))