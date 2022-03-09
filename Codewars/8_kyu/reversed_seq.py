def reverse_seq(n):
    return list(reversed(n))


print(reverse_seq([1,5,3,10,5]))


def reverseseq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output


print(reverseseq(5))


def reverseseq(n):
    return list(range(n, 0, -1))


print(reverseseq(10))
