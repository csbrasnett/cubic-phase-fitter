import numpy as np
from itertools import product
from string import ascii_lowercase
from .curvature import curvature

def curvature_calculation(surface_points, initial_transformed, result, cutting):
    # translate the surface points so that they're in the correct positions for the curvature calculation
    curvature_positions = np.array(surface_points + ((initial_transformed.mean(axis=0) - result.params['scale'].value )))

    # don't calculate curvature at every single point. every 10 works fine
    # curvatures = np.zeros(0)
    # for i in curvature_positions[cutting]:
    #     K = curvature(i[0], i[1], i[2], 1 / result.params['scale'].value)
    #     curvatures = np.append(curvatures, K)

    curvatures = curvature(curvature_positions[cutting].T[0],
                           curvature_positions[cutting].T[1],
                           curvature_positions[cutting].T[2],
                           1/result.params['scale'].value
                           )

    # hack to ensure we really have the same number of surface beads in each system.
    # the few values >0 are O(10-7) or so, so it's very small
    curvatures = -np.abs(curvatures)

    curvature_bins = np.linspace(-0.0012, 0, 50)
    curvature_bins = np.linspace(curvatures.min(),0,100)
    mids_curvature_bins = (curvature_bins[:-1] + curvature_bins[1:]) / 2

    inds = np.digitize(curvatures, curvature_bins)

    # makes a list of ['aa', 'ab', 'ac' ... 'zx', 'zy', 'zz']
    alpha = [''.join(list(i)) for i in product(ascii_lowercase, ascii_lowercase)]

    point_inds = np.zeros(0, dtype=int)
    opstr = []

    for i in range(1, curvature_bins.shape[0]):
        find = np.where(inds == i)[0].astype(int)
        point_inds = np.append(point_inds, find)
        opstr += [alpha[i]] * len(find)

    return curvatures, curvature_bins, mids_curvature_bins, point_inds, opstr
