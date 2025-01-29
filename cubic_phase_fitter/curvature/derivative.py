import numpy as np
from terms import *

def derivative(x, y, z, lamb):
    t1 =           term1(x, y, z, lamb)
    t2 =  0.1407 * term2(x, y, z, lamb)
    t3 =  0.0200 * term3(x, y, z, lamb)
    t4 = -0.0138 * term4(x, y, z, lamb)
    t5 = -0.0028 * term5(x, y, z, lamb)
    t6 = -0.0021 * term6(x, y, z, lamb)

    F_x_val  = np.array([t1[0], t2[0], t3[0], t4[0], t5[0], t6[0]]).sum()
    F_y_val  = np.array([t1[1], t2[1], t3[1], t4[1], t5[1], t6[1]]).sum()
    F_z_val  = np.array([t1[2], t2[2], t3[2], t4[2], t5[2], t6[2]]).sum()
    F_xx_val = np.array([t1[3], t2[3], t3[3], t4[3], t5[3], t6[3]]).sum()
    F_xy_val = np.array([t1[4], t2[4], t3[4], t4[4], t5[4], t6[4]]).sum()
    F_yy_val = np.array([t1[5], t2[5], t3[5], t4[5], t5[5], t6[5]]).sum()
    F_yz_val = np.array([t1[6], t2[6], t3[6], t4[6], t5[6], t6[6]]).sum()
    F_zz_val = np.array([t1[7], t2[7], t3[7], t4[7], t5[7], t6[7]]).sum()
    F_xz_val = np.array([t1[8], t2[8], t3[8], t4[8], t5[8], t6[8]]).sum()

    return np.array([F_x_val, F_y_val, F_z_val, F_xx_val, F_xy_val, F_yy_val, F_yz_val, F_zz_val, F_xz_val])
