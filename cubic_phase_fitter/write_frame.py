import numpy as np
from MDAnalysis import Universe


def write_frame(surface, frame_positions, cutting, point_inds, opstr,
                resindices, atomnames, resnames,
                time):

    sp_final = surface[cutting][point_inds]

    all_points = np.array(np.vstack((frame_positions, sp_final)))

    new_resids = np.concatenate((resindices,
                                 np.ones(sp_final.shape[0]) * (resindices[-1] + 1)))
    new_names = np.concatenate((atomnames, opstr))
    new_resnames = np.concatenate((resnames, np.array(['SUR'])))

    u1 = Universe.empty(n_atoms=all_points.shape[0],
                        n_residues=int(new_resids[-1]) + 1,
                        atom_resindex=new_resids,
                        trajectory=True
                        )

    u1.add_TopologyAttr('names', new_names)
    u1.add_TopologyAttr('resname', new_resnames)

    u1.load_new(all_points - sp_final.min(axis=0))

    dim = int(max(sp_final[:, 0]) - min(sp_final[:, 0]))
    u1.dimensions = [dim, dim, dim, 90, 90, 90]

    ag = u1.select_atoms('all')
    ag.write(f'frame_{time / 1e6 :.2f}.gro')

