#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:48:51 2025

@author: chris
"""
import argparse
from pathlib import Path

import MDAnalysis as mda
import numpy as np
from tqdm import tqdm
import pickle

from cubic_phase_fitter.curvature import curvature_calculation
from cubic_phase_fitter.fitter import fitter
from cubic_phase_fitter.translations import translations
from cubic_phase_fitter.point_generation import point_generator
from cubic_phase_fitter.write_frame import write_frame
from cubic_phase_fitter.molecule_curvature import molecule_curvature


def cubic_phase_fitter():

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', dest="trajectory", type=Path, default='prod.xtc', help="trajectory file to analyse")
    parser.add_argument('-s', dest="topology", type=Path, default='prod.tpr', help="trajectory file to analyse")
    parser.add_argument('-write-frame', dest='frame_writing', action='store_true', default=False,
                        help='write out frame containing fitted surface')
    parser.add_argument('-res', dest='target_resname', type=str, help="target resname of dopant lipid")
    parser.add_argument('-aname', dest='target_atomnames', type=str, nargs='*',
                        help=('target atomnames of dopant lipids for curvature distribution.'
                              'accepts multiple arguments for beads, eg -aname C4A C4B'))
    parser.add_argument('-curvature', dest='lipid_closest_point', action='store_true', default=False,
                        help='find the closest points on the surface to the input lipid')
    parser.add_argument('-ncells', dest='ncells', default=1, type=int,
                        help="number of unit cells in one direction to fit for (assumes cubic arrangement)")

    args = parser.parse_args()

    u = mda.Universe(args.topology, args.trajectory)

    resindices = u.atoms.resindices
    resnames = u.residues.resnames
    atomnames = u.atoms.names
    atom_resinds = u.residues.resindices

    terminal_MO_beads = u.select_atoms('resname MO and name C4A')

    if args.lipid_closest_point:
        target_indices = u.select_atoms(f'resname {args.target_resname} and name {" ".join(args.target_atomnames)}').atoms.indices

    if args.ncells == 4:
        terminal_MO_beads = terminal_MO_beads[np.linspace(0,terminal_MO_beads.n_atoms-1, 10000, dtype=int)]

    results = {}
    for ts in u.trajectory[::100]:
        result = fitter(terminal_MO_beads.positions, u.dimensions, args.ncells)

        if result is not None:
            initial_transformed = translations(result.params, u.atoms.positions)

            #find the points on the surface
            surface_points = point_generator(np.array(initial_transformed.mean(axis=0))[0], result.params['scale'].value,
                                             args.ncells)

            if surface_points is not None:
                # to guarantee we'll have 5000 points for the surface each time
                cutting = np.linspace(0, surface_points.shape[0] - 1, 100000, dtype=int)

                curvatures, curvature_bins, mids_curvature_bins, point_inds, opstr = curvature_calculation(surface_points,
                                                                                                           initial_transformed,
                                                                                                           result,
                                                                                                           cutting,
                                                                                                           args.ncells)
                # translate data and surface points so that they have the same origin at 0.
                #translate the surface points in the same way
                corrected_surface_points = (surface_points + surface_points.mean(axis=0))

                # translate the data points by the difference between half the lattice parameter and the mean positions
                corrected_data_points = initial_transformed - initial_transformed.mean(axis = 0) + corrected_surface_points.mean(axis=0)

                if args.frame_writing:
                    write_frame(corrected_surface_points, corrected_data_points,
                                cutting, point_inds, opstr,
                                resindices, atomnames, resnames, atom_resinds,
                                u.trajectory.time)

                if args.lipid_closest_point:
                    curvature_result = molecule_curvature(corrected_data_points, corrected_surface_points,
                                                          target_indices, curvatures, curvature_bins,
                                                          mids_curvature_bins, point_inds, cutting)

                    results[int(ts.time)] = curvature_result

    if args.lipid_closest_point:
        pickle.dump(results, open('results.p', 'wb'))

if __name__ == '__main__':
    cubic_phase_fitter()

