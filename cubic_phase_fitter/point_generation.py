import numpy as np
from .fitfunc.fitfunc import D_nodal_approx
from skimage import measure

def point_generator(pos, l, ncells):
    """
    Generate a D surface based on some input positions
    """
    print('generating surface')
    x_mean, y_mean, z_mean = pos

    try:
        # define the mgrid from which to generate the points
        if ncells == 1:
            X, Y, Z = np.mgrid[x_mean - (l/2):x_mean + (l/2):(l * 1j),
                               y_mean - (l/2):y_mean + (l/2):(l * 1j),
                               z_mean - (l/2):z_mean + (l/2):(l * 1j)]
        elif ncells == 2:
            X, Y, Z = np.mgrid[x_mean - l:x_mean + l:(l * 2j),
                               y_mean - l:y_mean + l:(l * 2j),
                               z_mean - l:z_mean + l:(l * 2j)]
        elif ncells == 4:
            X, Y, Z = np.mgrid[x_mean - (2*l):x_mean + (2*l):(l * 4j),
                               y_mean - (2*l):y_mean + (2*l):(l * 4j),
                               z_mean - (2*l):z_mean + (2*l):(l * 4j)]

    except MemoryError:
        return None

    lamb = 1 / l

    surf_eq = D_nodal_approx(X, Y, Z, lamb)
    # find vertices on the surface
    vertices, simplices, normals, values = measure.marching_cubes(surf_eq,0.0, spacing=np.array([10,10,10]))

    vertices = vertices/10

    # sort out the vertices and append them to the list of coordinates to write to file
    Xp, Yp, Zp = zip(*vertices)

    surface_points = np.array([Xp, Yp, Zp]).T #/ 10

    return surface_points
