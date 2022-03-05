def integrate(coefficient, exponent):
    return f'{coefficient // (exponent + 1)}x^{exponent + 1}'

print(integrate(3, 2))