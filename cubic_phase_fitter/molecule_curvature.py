import numpy as np
from scipy.spatial import KDTree

def molecule_curvature(corrected_data_points, corrected_surface_points, target_indices,
                       curvatures, curvature_bins, mids_curvature_bins, point_inds, cutting
                       ):

    sp_final = corrected_surface_points[cutting][point_inds]

    data_points = corrected_data_points - sp_final.min(axis=0)
    surface_points = sp_final - sp_final.min(axis=0)

    target_atom_pos = data_points[target_indices]

    tree = KDTree(surface_points, boxsize=surface_points.max(axis=0)+.1)  # small hack, but shouldn't affect substantially
    closest_distances, closest_surface_indices = tree.query(target_atom_pos, distance_upper_bound=50)

    '''
    take the curvatures that have been used for the final surface points
    digitize them
    extract the indices that have been found to be the closest to different tail points
    find the unique values and count them

    out[0] is +1 to the index of mids_curvature_bins
    out[1] is the count for that bin of curvature
    '''
    out = np.unique(np.digitize(curvatures[point_inds],
                                curvature_bins)[closest_surface_indices.astype(int)],
                    return_counts=True)

    curvature_result = (mids_curvature_bins, out,
                        np.histogram(curvatures[point_inds], curvature_bins)[0])

    return curvature_result