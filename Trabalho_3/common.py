
def apply_poly(x, betas):
    """
    For any polynomial function it applies that function to a given ``x``
    ``apply_poly(x, betas)``

    ``x`` -> a given number, or ``numpy``s array of numbers.

    ``betas`` -> a list of values describing each power values.

    i.e.:
        ``y = m1 * x^n1 + m2 * x^n2``
        ``[m1, m2]``

    e.g.:
        ``y = x^0 + 5x^1``
        ``[1, 5]``

    """
    enum_betas = enumerate(reversed(betas))
    value = sum([x ** exp * beta for exp, beta in enum_betas])
    return value


