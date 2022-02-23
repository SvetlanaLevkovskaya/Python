"""Write a comparator for a list of phonetic words for the letters of the greek alphabet."""

greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the global namespace
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)


print(greek_comparator('alpha', 'beta'))
print(greek_comparator('psi', 'psi'))
print(greek_comparator('upsilon', 'rho'))
