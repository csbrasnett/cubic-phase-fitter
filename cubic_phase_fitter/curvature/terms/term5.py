import numpy as np

def term5(x, y, z, m):
    pi = np.pi
    # t5_x
    cg = (-2 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
          10 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi * m * np.sin(5 * pi * m * x) -
          2 * np.cos(pi * m * z) * pi * m * np.sin(pi * m * x) * np.cos(5 * pi * m * y) -
          2 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) +
          10 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(5 * pi * m * x) +
          2 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(5 * pi * m * y) +
          2 * pi * m * np.cos(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) +
          10 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi * m * np.cos(5 * pi * m * x) -
          2 * np.sin(pi * m * z) * pi * m * np.sin(pi * m * x) * np.sin(5 * pi * m * y) +
          2 * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) -
          10 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi * m * np.sin(5 * pi * m * x) +
          2 * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) * np.cos(5 * pi * m * y))

    # t5_y
    cg0 = (-2 * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi * m * np.cos(5 * pi * m * x) -
           10 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(5 * pi * m * y) +
           2 * pi * m * np.cos(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi * m * np.sin(5 * pi * m * x) +
           10 * np.cos(pi * m * z) * pi * m * np.sin(pi * m * x) * np.cos(5 * pi * m * y) -
           2 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) +
           2 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi * m * np.sin(5 * pi * m * x) +
           10 * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) * np.cos(5 * pi * m * y) +
           2 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) +
           2 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(5 * pi * m * x) -
           10 * np.sin(pi * m * z) * pi * m * np.sin(pi * m * x) * np.sin(5 * pi * m * y))

    # t5_z
    cg1 = (-10 * pi * m * np.cos(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) -
           2 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi * m * np.cos(5 * pi * m * x) -
           2 * np.sin(pi * m * z) * pi * m * np.cos(pi * m * x) * np.cos(5 * pi * m * y) +
           10 * pi * m * np.cos(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) +
           2 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi * m * np.sin(5 * pi * m * x) -
           2 * np.sin(pi * m * z) * pi * m * np.sin(pi * m * x) * np.sin(5 * pi * m * y) +
           10 * pi * m * np.sin(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi * m * np.sin(5 * pi * m * x) +
           2 * np.cos(pi * m * z) * pi * m * np.cos(pi * m * x) * np.sin(5 * pi * m * y) -
           10 * pi * m * np.sin(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) +
           2 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi * m * np.cos(5 * pi * m * x) +
           2 * np.cos(pi * m * z) * pi * m * np.sin(pi * m * x) * np.cos(5 * pi * m * y))

    # t5_xx
    cg2 = (-2 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
           50 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           2 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) -
           50 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           2 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) -
           50 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           2 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) -
           50 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           2 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(5 * pi * m * y))

    # t5_xy
    cg3 = (2 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) +
           10 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) +
           10 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) -
           10 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) +
           10 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) +
           10 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           10 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(5 * pi * m * y) +
           2 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
           10 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           10 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(5 * pi * m * y))

    # t5_yy
    cg4 = (-2 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           50 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) -
           2 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           50 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           50 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(5 * pi * m * y) -
           2 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           50 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(5 * pi * m * y))

    # t5_yz
    cg5 = (10 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) +
           2 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) +
           10 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(5 * pi * m * y) +
           10 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           10 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(5 * pi * m * y) -
           10 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) +
           10 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(5 * pi * m * y) -
           10 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) +
           2 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           10 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(5 * pi * m * y))

    # t5_zz
    cg6 = (-50 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           2 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(5 * pi * m * y) -
           50 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) -
           2 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           2 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(5 * pi * m * y) -
           50 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) -
           2 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(5 * pi * m * y) -
           50 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) -
           2 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           2 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(5 * pi * m * y))

    # t5_xz
    cg7 = (10 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(pi * m * y) * np.sin(5 * pi * m * z) +
           10 * np.cos(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) +
           2 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.cos(5 * pi * m * y) -
           10 * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(pi * m * y) * np.cos(5 * pi * m * z) +
           10 * np.cos(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           2 * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(5 * pi * m * y) +
           10 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(pi * m * y) * np.cos(5 * pi * m * z) -
           10 * np.sin(pi * m * y) * np.sin(pi * m * z) * pi ** 2 * m ** 2 * np.cos(5 * pi * m * x) -
           2 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(pi * m * x) * np.sin(5 * pi * m * y) -
           10 * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.sin(pi * m * y) * np.sin(5 * pi * m * z) -
           10 * np.sin(pi * m * y) * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.sin(5 * pi * m * x) +
           2 * np.cos(pi * m * z) * pi ** 2 * m ** 2 * np.cos(pi * m * x) * np.cos(5 * pi * m * y))

    return np.array([cg, cg0, cg1, cg2, cg3, cg4, cg5, cg6, cg7])
