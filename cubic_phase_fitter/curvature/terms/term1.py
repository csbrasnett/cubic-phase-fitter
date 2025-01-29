import numpy as np

def term1(x ,y ,z ,m):
    pi = np.pi
    # t1_x
    cg = (-3 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
          3 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
          3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) +
          3 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y))

    # t1_y
    cg0 = (-3 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y) +
           3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) -
           3 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
           3 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z))

    # t1_z
    cg1 = (-3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) +
           3 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y) +
           3 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           3 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z))

    # t1_xx
    cg2 = (-3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) -
           3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           3 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y))

    # t1_xy
    cg3 = (3 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) -
           3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z))

    # t1_yy
    cg4 = (-3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) -
           3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           3 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y))

    # t1_yz
    cg5 = (3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) +
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           3 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) -
           3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x))

    # t1_zz
    cg6 = (-3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z) -
           3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           3 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y))

    # t1_xz
    cg7 = (3 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) -
           3 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) +
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(pi * m * z) -
           3 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(pi * m * z))

    return np.array([cg, cg0, cg1, cg2, cg3, cg4, cg5, cg6, cg7])
