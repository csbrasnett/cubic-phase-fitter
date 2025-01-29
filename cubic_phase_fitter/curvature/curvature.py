import numpy as np
from .derivative import derivative

def nominator(vals):
    # for each input, m has a slice as:
    # m = np.array([[F_xx, F_xy, F_xz, F_x],
    #               [F_xy, F_yy, F_yz, F_y],
    #               [F_xz, F_yz, F_zz, F_z],
    #               [F_x, F_y, F_z, 0]])
    m = np.array([[vals[:, 3], vals[:, 4], vals[:, 8], vals[:, 0]],
                  [vals[:, 4], vals[:, 5], vals[:, 6], vals[:, 1]],
                  [vals[:, 8], vals[:, 6], vals[:, 7], vals[:, 2]],
                  [vals[:, 0], vals[:, 1], vals[:, 2], np.zeros(len(vals[:, 0]))],
                  ])

    d = np.array([np.linalg.det(i) for i in m.T])

    return d

def denominator(vals):
    g = np.array([vals[:, 0], vals[:, 1], vals[:, 2]])
    mag_g = np.array([np.linalg.norm(i)**4 for i in g.T])
    return mag_g

def curvature(x, y, z, lamb):
    '''
    x,y,z are the spatial positions, lamb is the lambda of the cubic phase

    the derivative function was worked out by hand. do not do it again, for your own sanity.
    '''
    derivatives = derivative(x, y, z, lamb)

    n = nominator(derivatives)
    d = denominator(derivatives)
    K = -(n / d)

    return K
