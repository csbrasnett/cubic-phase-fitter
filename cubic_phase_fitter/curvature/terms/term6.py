import numpy as np

def term6(x ,y ,z ,m):
    pi = np.pi
    # t6_x
    cg = (-18 * pi * m * np.sin(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z) -
          18 * pi * m * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z) +
          18 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi * m * np.cos(3 * pi * m * x) +
          18 * np.cos(3 * pi * m * z) * pi * m * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y))

    # t6_y
    cg0 = (-18 * np.cos(3 * pi * m * z) * pi * m * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) +
           18 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi * m * np.cos(3 * pi * m * x) -
           18 * pi * m * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z) +
           18 * pi * m * np.sin(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z))

    # t6_z
    cg1 = (-18 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi * m * np.cos(3 * pi * m * x) +
           18 * np.cos(3 * pi * m * z) * pi * m * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) +
           18 * pi * m * np.sin(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z) -
           18 * pi * m * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z))

    # t6_xx
    cg2 = (-54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z) -
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z) -
           54 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           54 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y))

    # t6_xy
    cg3 = (54 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y) -
           54 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z) +
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z))

    # t6_yy
    cg4 = (-54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z) -
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z) -
           54 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           54 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y))

    # t6_yz
    cg5 = (54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z) +
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z) -
           54 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y) -
           54 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x))

    # t6_zz
    cg6 = (-54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z) -
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z) -
           54 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           54 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y))

    # t6_xz
    cg7 = (54 * np.cos(3 * pi * m * y) * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           54 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(3 * pi * m * y) +
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(3 * pi * m * y) * np.cos(3 * pi * m * z) -
           54 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(3 * pi * m * y) * np.sin(3 * pi * m * z))

    return np.array([cg, cg0, cg1, cg2, cg3, cg4, cg5, cg6, cg7])
