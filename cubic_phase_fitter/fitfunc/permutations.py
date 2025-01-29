import numpy as np

'''these initial functions are all associated with fitting minimal surface nodal approximations'''

def trig_choose(a, var):
    if a == 's':
        return np.sin(var)
    if a == 'c':
        return np.cos(var)


def O_pqr(p, q, r, h, k, l, x, y, z, lamb):
    X = lamb * np.pi * x
    Y = lamb * np.pi * y
    Z = lamb * np.pi * z

    term_1 = trig_choose(p, (h * X)) * trig_choose(q, (k * Z)) * trig_choose(r, (l * Y))
    term_2 = trig_choose(p, (h * Y)) * trig_choose(q, (k * X)) * trig_choose(r, (l * Z))
    term_3 = trig_choose(p, (h * Z)) * trig_choose(q, (k * Y)) * trig_choose(r, (l * X))

    return term_1 + term_2 + term_3


def E_pqr(p, q, r, h, k, l, x, y, z, lamb):
    X = lamb * np.pi * x
    Y = lamb * np.pi * y
    Z = lamb * np.pi * z

    term_1 = trig_choose(p, (h * X)) * trig_choose(q, (k * Y)) * trig_choose(r, (l * Z))
    term_2 = trig_choose(p, (h * Y)) * trig_choose(q, (k * Z)) * trig_choose(r, (l * X))
    term_3 = trig_choose(p, (h * Z)) * trig_choose(q, (k * X)) * trig_choose(r, (l * Y))

    return term_1 + term_2 + term_3


def permE1(h, k, l, x, y, z, lamb):
    return E_pqr('c', 'c', 'c', h, k, l, x, y, z, lamb)


def permE2(h, k, l, x, y, z, lamb):
    return E_pqr('c', 's', 's', h, k, l, x, y, z, lamb)


def permE3(h, k, l, x, y, z, lamb):
    return E_pqr('s', 'c', 's', h, k, l, x, y, z, lamb)


def permE4(h, k, l, x, y, z, lamb):
    return E_pqr('s', 's', 'c', h, k, l, x, y, z, lamb)


def permE5(h, k, l, x, y, z, lamb):
    return E_pqr('s', 'c', 'c', h, k, l, x, y, z, lamb)


def permE6(h, k, l, x, y, z, lamb):
    return E_pqr('c', 's', 'c', h, k, l, x, y, z, lamb)


def permE7(h, k, l, x, y, z, lamb):
    return E_pqr('s', 's', 's', h, k, l, x, y, z, lamb)


def permE8(h, k, l, x, y, z, lamb):
    return E_pqr('c', 'c', 's', h, k, l, x, y, z, lamb)


def permO1(h, k, l, x, y, z, lamb):
    return O_pqr('c', 'c', 'c', h, k, l, x, y, z, lamb)


def permO2(h, k, l, x, y, z, lamb):
    return O_pqr('c', 's', 's', h, k, l, x, y, z, lamb)


def permO3(h, k, l, x, y, z, lamb):
    return O_pqr('s', 'c', 's', h, k, l, x, y, z, lamb)


def permO4(h, k, l, x, y, z, lamb):
    return O_pqr('s', 's', 'c', h, k, l, x, y, z, lamb)


def permO5(h, k, l, x, y, z, lamb):
    return O_pqr('c', 's', 'c', h, k, l, x, y, z, lamb)


def permO6(h, k, l, x, y, z, lamb):
    return O_pqr('c', 'c', 's', h, k, l, x, y, z, lamb)


def permO7(h, k, l, x, y, z, lamb):
    return O_pqr('s', 's', 's', h, k, l, x, y, z, lamb)


def permO8(h, k, l, x, y, z, lamb):
    return O_pqr('s', 'c', 'c', h, k, l, x, y, z, lamb)
