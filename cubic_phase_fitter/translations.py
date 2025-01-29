import numpy as np

def translations(result_params, pos):
    trans_a = result_params['trans_a'].value
    trans_b = result_params['trans_b'].value
    trans_c = result_params['trans_c'].value
    rot_a = result_params['rot_a'].value
    rot_b = result_params['rot_b'].value
    rot_c = result_params['rot_c'].value

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

    rot_z = np.matrix([[np.cos(rot_c), -np.sin(rot_c), 0]
                          , [np.sin(rot_c), np.cos(rot_c), 0],
                       [0, 0, 1]])

    rot = rot_z * rot_y * rot_x  # nb! this order matters!

    # perform the coordinate transformation.
    transformation = rot * (pos.T + translational_matrix)

    return transformation.T
