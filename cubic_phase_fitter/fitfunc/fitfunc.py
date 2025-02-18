import numpy as np
from .permutations import permO1, permO2, permO3, permO4, permE1, permE2, permE3, permE4

def D_nodal_approx(x, y, z, lamb):
    term1 = (permE1(1, 1, 1, x, y, z, lamb) +
             permE2(1, 1, 1, x, y, z, lamb) +
             permE3(1, 1, 1, x, y, z, lamb) +
             permE4(1, 1, 1, x, y, z, lamb))

    term2 = 0.1407 * (permE1(1, 1, 1, x, y, z, lamb) + permE2(1, 1, 1, x, y, z, lamb) +
                      permE3(1, 1, 1, x, y, z, lamb) + permE4(1, 1, 1, x, y, z, lamb) +
                      permO1(1, 1, 1, x, y, z, lamb) + permO2(1, 1, 1, x, y, z, lamb) +
                      permO3(1, 1, 1, x, y, z, lamb) + permO4(1, 1, 1, x, y, z, lamb))

    term3 = 0.0200 * (permE1(3, 1, 1, x, y, z, lamb) + permE2(3, 1, 1, x, y, z, lamb) -
                      permE3(3, 1, 1, x, y, z, lamb) + permE4(3, 1, 1, x, y, z, lamb) +
                      permO1(3, 1, 1, x, y, z, lamb) + permO2(3, 1, 1, x, y, z, lamb) -
                      permO3(3, 1, 1, x, y, z, lamb) - permO4(3, 1, 1, x, y, z, lamb))

    term4 = 0.0138 * (permE1(3, 1, 3, x, y, z, lamb) - permE2(3, 1, 3, x, y, z, lamb) +
                      permE3(3, 1, 3, x, y, z, lamb) - permE4(3, 1, 3, x, y, z, lamb) +
                      permO1(3, 1, 3, x, y, z, lamb) - permO2(3, 1, 3, x, y, z, lamb) +
                      permO3(3, 1, 3, x, y, z, lamb) + permO4(3, 1, 3, x, y, z, lamb))

    term5 = 0.0028 * (permE1(1, 1, 5, x, y, z, lamb) + permE2(1, 1, 5, x, y, z, lamb) +
                      permE3(1, 1, 5, x, y, z, lamb) + permE4(1, 1, 5, x, y, z, lamb) +
                      permO1(1, 1, 5, x, y, z, lamb) + permO2(1, 1, 5, x, y, z, lamb) +
                      permO3(1, 1, 5, x, y, z, lamb) + permO4(1, 1, 5, x, y, z, lamb))

    term6 = 0.0021 * (permE1(3, 3, 3, x, y, z, lamb) + permE2(3, 3, 3, x, y, z, lamb) +
                      permE3(3, 3, 3, x, y, z, lamb) + permE4(3, 3, 3, x, y, z, lamb) +
                      permO1(3, 3, 3, x, y, z, lamb) + permO2(3, 3, 3, x, y, z, lamb) +
                      permO3(3, 3, 3, x, y, z, lamb) + permO4(3, 3, 3, x, y, z, lamb))

    term7 = 0.0001 * (permE1(3, 1, 5, x, y, z, lamb) + permE2(3, 1, 5, x, y, z, lamb) -
                      permE3(3, 1, 5, x, y, z, lamb) - permE4(3, 1, 5, x, y, z, lamb) +
                      permO1(3, 1, 5, x, y, z, lamb) + permO2(3, 1, 5, x, y, z, lamb) -
                      permO3(3, 1, 5, x, y, z, lamb) - permO4(3, 1, 5, x, y, z, lamb))

    return term1 + term2 + term3 - term4 - term5 - term6 + term7


# function to fit the surface to
def fitfunc(params, pos, alt_return=False):
    trans_a = params['trans_a']
    trans_b = params['trans_b']
    trans_c = params['trans_c']
    rot_a = params['rot_a']
    rot_b = params['rot_b']
    rot_c = params['rot_c']
    scale = params['scale']

    # set up the translation
    translational_matrix = np.matrix(np.array(np.ones_like(pos).T) * np.array([[trans_a],
                                                                               [trans_b],
                                                                               [trans_c]]))

    # set up the rotation
    rot_x = np.matrix([[1, 0, 0],
                       [0, np.cos(rot_a), -np.sin(rot_a)],
                       [0, np.sin(rot_a), np.cos(rot_a)]])

    rot_y = np.matrix([[np.cos(rot_b), 0, np.sin(rot_b)],
                       [0, 1, 0],
                       [-np.sin(rot_b), 0, np.cos(rot_b)]])

    rot_z = np.matrix([[np.cos(rot_c), -np.sin(rot_c), 0],
                       [np.sin(rot_c), np.cos(rot_c), 0],
                       [0, 0, 1]])

    rot = rot_z * rot_y * rot_x  # nb! this order matters!

    # perform the coordinate transformation.
    transformation = rot * (pos.T + translational_matrix)

    # try to fit a D surface depending on an initial guess
    C_i = D_nodal_approx(transformation[0].A[0],
                         transformation[1].A[0],
                         transformation[2].A[0],
                         1 / scale)
    if alt_return:
        return C_i
    else:
        # evaluate how well the function has been fitted
        C_i_squared = np.square(C_i)

        return C_i_squared