import numpy as np

def term2(x ,y ,z ,m):
    pi = np.pi
    # t2_x
    cg = (-6 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
          6 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
          6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) +
          6 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y))

    # t2_y
    cg0 = (-6 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y) +
           6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) -
           6 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
           6 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z))

    # t2_z
    cg1 = (-6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) +
           6 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y) +
           6 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           6 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z))

    # t2_xx
    cg2 = (-6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) -
           6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           6 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y))

    # t2_xy
    cg3 = (6 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) -
           6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z))

    # t2_yy
    cg4 = (-6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) -
           6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           6 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y))

    # t2_yz
    cg5 = (6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           6 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) -
           6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x))

    # t2_zz
    cg6 = (-6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) -
           6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           6 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y))

    # t2_xz
    cg7 = (6 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           6 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) +
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           6 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z))

    return np.array([cg, cg0, cg1, cg2, cg3, cg4, cg5, cg6, cg7])
