import numpy as np

def term4(x ,y ,z ,m):
    pi = np.pi
    # t4_x
    cg = (-6 * pi * m * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) -
          6 * np.cos(3 * pi * m * y) * np.cos(pi * m * z) * pi * m * np.sin(3 * pi * m * x) -
          2 * np.cos(3 * pi * m * z) * pi * m * np.sin(pi * m * x) * np.cos(3 * pi * m * y) +
          6 * pi * m * np.cos(3 * pi * m * x) * np.cos(pi * m * y) * np.sin(3 * pi * m * z) +
          6 * np.sin(3 * pi * m * y) * np.cos(pi * m * z) * pi * m * np.cos(3 * pi * m * x) -
          2 * np.sin(3 * pi * m * z) * pi * m * np.sin(pi * m * x) * np.sin(3 * pi * m * y) -
          6 * pi * m * np.cos(3 * pi * m * x) * np.sin(pi * m * y) * np.cos(3 * pi * m * z) +
          6 * np.sin(3 * pi * m * y) * np.sin(pi * m * z) * pi * m * np.sin(3 * pi * m * x) -
          2 * np.sin(3 * pi * m * z) * pi * m * np.cos(pi * m * x) * np.cos(3 * pi * m * y))

    # t4_y
    cg0 = (-2 * pi * m * np.cos(3 * pi * m * x) * np.sin(pi * m * y) * np.cos(3 * pi * m * z) -
           6 * np.sin(3 * pi * m * y) * np.cos(pi * m * z) * pi * m * np.cos(3 * pi * m * x) -
           6 * np.cos(3 * pi * m * z) * np.cos(pi * m * x) * pi * m * np.sin(3 * pi * m * y) -
           2 * np.sin(3 * pi * m * x) * pi * m * np.sin(pi * m * y) * np.sin(3 * pi * m * z) +
           6 * np.cos(3 * pi * m * y) * np.cos(pi * m * z) * pi * m * np.sin(3 * pi * m * x) +
           6 * np.sin(3 * pi * m * z) * pi * m * np.cos(pi * m * x) * np.cos(3 * pi * m * y) -
           2 * pi * m * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) -
           6 * pi * m * np.cos(3 * pi * m * y) * np.sin(pi * m * z) * np.cos(3 * pi * m * x) +
           6 * np.sin(3 * pi * m * z) * pi * m * np.sin(pi * m * x) * np.sin(3 * pi * m * y))

    # t4_z
    cg1 = (-6 * pi * m * np.cos(3 * pi * m * x) * np.cos(pi * m * y) * np.sin(3 * pi * m * z) -
           2 * pi * m * np.cos(3 * pi * m * y) * np.sin(pi * m * z) * np.cos(3 * pi * m * x) -
           6 * np.sin(3 * pi * m * z) * pi * m * np.cos(pi * m * x) * np.cos(3 * pi * m * y) +
           6 * pi * m * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) -
           2 * np.sin(3 * pi * m * y) * np.sin(pi * m * z) * pi * m * np.sin(3 * pi * m * x) +
           6 * np.cos(3 * pi * m * z) * np.cos(pi * m * x) * pi * m * np.sin(3 * pi * m * y) +
           6 * np.sin(3 * pi * m * x) * pi * m * np.sin(pi * m * y) * np.sin(3 * pi * m * z) -
           2 * np.sin(3 * pi * m * y) * np.cos(pi * m * z) * pi * m * np.cos(3 * pi * m * x) -
           6 * np.cos(3 * pi * m * z) * pi * m * np.sin(pi * m * x) * np.cos(3 * pi * m * y))

    # t4_xx
    cg2 = (-18 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) -
           18 * np.cos(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) -
           2 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(3 * pi * m * y) -
           18 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.sin(3 * pi * m * z) -
           18 * np.sin(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           2 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(3 * pi * m * y) +
           18 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(pi * m * y) * np.cos(3 * pi * m * z) +
           18 * np.sin(3 * pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) +
           2 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(3 * pi * m * y))

    # t4_xy
    cg3 = (6 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(pi * m * y) * np.cos(3 * pi * m * z) +
           18 * np.sin(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) +
           6 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(3 * pi * m * y) -
           6 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(pi * m * y) * np.sin(3 * pi * m * z) +
           18 * np.cos(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) -
           6 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(3 * pi * m * y) -
           6 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) +
           18 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * y) * np.sin(pi * m * z) * np.sin(3 * pi * m * x) +
           6 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(3 * pi * m * y))

    # t4_yy
    cg4 = (-2 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) -
           18 * np.cos(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) -
           18 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(3 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.sin(3 * pi * m * z) -
           18 * np.sin(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           18 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(3 * pi * m * y) +
           2 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(pi * m * y) * np.cos(3 * pi * m * z) +
           18 * np.sin(3 * pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) +
           18 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(3 * pi * m * y))

    # t4_yz
    cg5 = (6 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.sin(pi * m * y) * np.sin(3 * pi * m * z) +
           6 * np.sin(3 * pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) +
           18 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(3 * pi * m * y) -
           6 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(pi * m * y) * np.cos(3 * pi * m * z) -
           6 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * y) * np.sin(pi * m * z) * np.sin(3 * pi * m * x) +
           18 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(3 * pi * m * y) +
           6 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.sin(3 * pi * m * z) -
           6 * np.cos(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) +
           18 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(3 * pi * m * y))

    # t4_zz
    cg6 = (-18 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) -
           2 * np.cos(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) -
           18 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(3 * pi * m * y) -
           18 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.sin(3 * pi * m * z) -
           2 * np.sin(3 * pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) -
           18 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(3 * pi * m * y) +
           18 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.sin(pi * m * y) * np.cos(3 * pi * m * z) +
           2 * np.sin(3 * pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) +
           18 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(3 * pi * m * y))

    # t4_xz
    cg7 = (18 * pi ** 2 * m ** 2 * np.sin(3 * pi * m * x) * np.cos(pi * m * y) * np.sin(3 * pi * m * z) +
           6 * np.cos(3 * pi * m * y) * pi ** 2 * m ** 2 * np.sin(pi * m * z) * np.sin(3 * pi * m * x) +
           6 * np.sin(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(3 * pi * m * y) +
           18 * pi ** 2 * m ** 2 * np.cos(3 * pi * m * x) * np.cos(pi * m * y) * np.cos(3 * pi * m * z) -
           6 * np.sin(3 * pi * m * y) * pi ** 2 * m ** 2 * np.sin(pi * m * z) * np.cos(3 * pi * m * x) -
           6 * np.cos(3 * pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(3 * pi * m * y))

    return np.array([cg, cg0, cg1, cg2, cg3, cg4, cg5, cg6, cg7])
