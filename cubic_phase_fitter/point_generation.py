import numpy as np
from .fitfunc.fitfunc import D_nodal_approx
from skimage import measure

def point_generator(pos, l):
    '''
    Generate a D surface based on some input positions
    '''

    x_mean = pos[0]
    y_mean = pos[1]
    z_mean = pos[2]

    # define the mgrid from which to generate the points
    X, Y, Z = np.mgrid[x_mean - (l / 2):x_mean + (l / 2):(l * 1j),
              y_mean - (l / 2):y_mean + (l / 2):(l * 1j),
              z_mean - (l / 2):z_mean + (l / 2):(l * 1j)]

    lamb = 1 / l

    surf_eq = D_nodal_approx(X, Y, Z, lamb)
    try:
        # find vertices on the surface
        vertices, simplices, normals, values = measure.marching_cubes(surf_eq)
    except MemoryError:
        return None

    # sort out the vertices and append them to the list of coordinates to write to file
    Xp, Yp, Zp = zip(*vertices)

    surface_points = np.array([Xp, Yp, Zp]).T

    return surface_points

