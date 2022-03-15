from scipy.special import comb


def easyline(n):
    return comb(2 * n, n, exact=True)


print(easyline(4))


def easyline(n):
    return easyline(n-1)*(4*n-2)//n if n else 1


print(easyline(4))
