import numpy as np
from .fitfunc.fitfunc import D_nodal_approx
from skimage import measure
from MDAnalysis import Universe

def point_generator(pos, l):
    """
    Generate a D surface based on some input positions
    """

    x_mean, y_mean, z_mean = pos

    try:
        # define the mgrid from which to generate the points
        # X, Y, Z = np.mgrid[x_mean - (l/2):x_mean + (l/2):(l * 1j),
        #                    y_mean - (l/2):y_mean + (l/2):(l * 1j),
        #                    z_mean - (l/2):z_mean + (l/2):(l * 1j)]
        X, Y, Z = np.mgrid[x_mean - l:x_mean + l:(l * 2j),
                           y_mean - l:y_mean + l:(l * 2j),
                           z_mean - l:z_mean + l:(l * 2j)]
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

    # u = Universe.empty(n_atoms=surface_points.shape[0],
    #                     n_residues=1,
    #                     atom_resindex=np.arange(len(surface_points)),
    #                     trajectory=True
    #                     )
    # u.load_new(surface_points)
    # dim = int(max(surface_points.T[0] - min(surface_points.T[0])))
    # u.dimensions = [dim, dim, dim, 90, 90, 90]
    # ag = u.select_atoms('all')
    # ag.write('test.gro')



    return surface_points
