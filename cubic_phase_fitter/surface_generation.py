#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:07:46 2023

@author: chris
"""

import numpy as np
from skimage import measure
import open3d as o3d
import argparse

'''these initial functions are all associated with fitting minimal surface nodal approximations'''
def trig_choose(a,var):
    if a == 's':
        return np.sin(var)
    if a == 'c':
        return np.cos(var)

def O_pqr(p,q,r,h,k,l,x,y,z,lamb):
    X=lamb*np.pi*x
    Y=lamb*np.pi*y
    Z=lamb*np.pi*z

    term_1=trig_choose(p,(h*X))*trig_choose(q,(k*Z))*trig_choose(r,(l*Y))
    term_2=trig_choose(p,(h*Y))*trig_choose(q,(k*X))*trig_choose(r,(l*Z))
    term_3=trig_choose(p,(h*Z))*trig_choose(q,(k*Y))*trig_choose(r,(l*X))

    return term_1+term_2+term_3

def E_pqr(p,q,r,h,k,l,x,y,z,lamb):
    X=lamb*np.pi*x
    Y=lamb*np.pi*y
    Z=lamb*np.pi*z

    term_1=trig_choose(p,(h*X))*trig_choose(q,(k*Y))*trig_choose(r,(l*Z))
    term_2=trig_choose(p,(h*Y))*trig_choose(q,(k*Z))*trig_choose(r,(l*X))
    term_3=trig_choose(p,(h*Z))*trig_choose(q,(k*X))*trig_choose(r,(l*Y))

    return term_1+term_2+term_3

def permE1(h,k,l,x,y,z,lamb):
    return E_pqr('c','c','c',h,k,l,x,y,z,lamb)

def permE2(h,k,l,x,y,z,lamb):
    return E_pqr('c','s','s',h,k,l,x,y,z,lamb)

def permE3(h,k,l,x,y,z,lamb):
    return E_pqr('s','c','s',h,k,l,x,y,z,lamb)

def permE4(h,k,l,x,y,z,lamb):
    return E_pqr('s','s','c',h,k,l,x,y,z,lamb)

def permE5(h,k,l,x,y,z,lamb):
    return E_pqr('s','c','c',h,k,l,x,y,z,lamb)

def permE6(h,k,l,x,y,z,lamb):
    return E_pqr('c','s','c',h,k,l,x,y,z,lamb)

def permE7(h,k,l,x,y,z,lamb):
    return E_pqr('s','s','s',h,k,l,x,y,z,lamb)

def permE8(h,k,l,x,y,z,lamb):
    return E_pqr('c','c','s',h,k,l,x,y,z,lamb)

def permO1(h,k,l,x,y,z,lamb):
    return O_pqr('c','c','c',h,k,l,x,y,z,lamb)

def permO2(h,k,l,x,y,z,lamb):
    return O_pqr('c','s','s',h,k,l,x,y,z,lamb)

def permO3(h,k,l,x,y,z,lamb):
    return O_pqr('s','c','s',h,k,l,x,y,z,lamb)

def permO4(h,k,l,x,y,z,lamb):
    return O_pqr('s','s','c',h,k,l,x,y,z,lamb)

def permO5(h,k,l,x,y,z,lamb):
    return O_pqr('c','s','c',h,k,l,x,y,z,lamb)

def permO6(h,k,l,x,y,z,lamb):
    return O_pqr('c','c','s',h,k,l,x,y,z,lamb)

def permO7(h,k,l,x,y,z,lamb):
    return O_pqr('s','s','s',h,k,l,x,y,z,lamb)

def permO8(h,k,l,x,y,z,lamb):
    return O_pqr('s','c','c',h,k,l,x,y,z,lamb)

def G_surf_eq(X,Y,Z, lamb):

    term1=(permE5(1,1,0,X,Y,Z,lamb)+permO5(1,1,0,X,Y,Z,lamb))

    term2=0.3435*(permE5(1,1,0,X,Y,Z,lamb)+permO5(1,1,0,X,Y,Z,lamb))

    term3=0.0202*(permE6(0,3,1,X,Y,Z,lamb)+permO6(0,3,1,X,Y,Z,lamb))

    term4=0.0106*(permE7(2,2,2,X,Y,Z,lamb)-permO7(2,2,2,X,Y,Z,lamb))

    term5=0.0298*(permE6(2,1,3,X,Y,Z,lamb)+permO6(2,1,3,X,Y,Z,lamb))

    term6=0.0016*(permE8(3,0,3,X,Y,Z,lamb)+permO8(3,0,3,X,Y,Z,lamb))

    term7=0.0011*(permE5(1,1,4,X,Y,Z,lamb)+permO5(1,1,4,X,Y,Z,lamb))

    surf_eq = term1+term2-term3-term4+term5+term6-term7

    return surf_eq

def D_surf_eq(X,Y,Z, lamb):
    term1=(permE1(1,1,1,X,Y,Z,lamb)+
           permE2(1,1,1,X,Y,Z,lamb)+
           permE3(1,1,1,X,Y,Z,lamb)+
           permE4(1,1,1,X,Y,Z,lamb))

    term2=0.1407*(permE1(1,1,1,X,Y,Z,lamb)+permE2(1,1,1,X,Y,Z,lamb)+
                  permE3(1,1,1,X,Y,Z,lamb)+permE4(1,1,1,X,Y,Z,lamb)+
                  permO1(1,1,1,X,Y,Z,lamb)+permO2(1,1,1,X,Y,Z,lamb)+
                  permO3(1,1,1,X,Y,Z,lamb)+permO4(1,1,1,X,Y,Z,lamb))

    term3=0.0200*(permE1(3,1,1,X,Y,Z,lamb)+permE2(3,1,1,X,Y,Z,lamb)-
                  permE3(3,1,1,X,Y,Z,lamb)+permE4(3,1,1,X,Y,Z,lamb)+
                  permO1(3,1,1,X,Y,Z,lamb)+permO2(3,1,1,X,Y,Z,lamb)-
                  permO3(3,1,1,X,Y,Z,lamb)-permO4(3,1,1,X,Y,Z,lamb))

    term4=0.0138*(permE1(3,1,3,X,Y,Z,lamb)-permE2(3,1,3,X,Y,Z,lamb)+
                  permE3(3,1,3,X,Y,Z,lamb)-permE4(3,1,3,X,Y,Z,lamb)+
                  permO1(3,1,3,X,Y,Z,lamb)-permO2(3,1,3,X,Y,Z,lamb)+
                  permO3(3,1,3,X,Y,Z,lamb)+permO4(3,1,3,X,Y,Z,lamb))

    term5=0.0028*(permE1(1,1,5,X,Y,Z,lamb)+permE2(1,1,5,X,Y,Z,lamb)+
                  permE3(1,1,5,X,Y,Z,lamb)+permE4(1,1,5,X,Y,Z,lamb)+
                  permO1(1,1,5,X,Y,Z,lamb)+permO2(1,1,5,X,Y,Z,lamb)+
                  permO3(1,1,5,X,Y,Z,lamb)+permO4(1,1,5,X,Y,Z,lamb))

    term6=0.0021*(permE1(3,3,3,X,Y,Z,lamb)+permE2(3,3,3,X,Y,Z,lamb)+
                  permE3(3,3,3,X,Y,Z,lamb)+permE4(3,3,3,X,Y,Z,lamb)+
                  permO1(3,3,3,X,Y,Z,lamb)+permO2(3,3,3,X,Y,Z,lamb)+
                  permO3(3,3,3,X,Y,Z,lamb)+permO4(3,3,3,X,Y,Z,lamb))

    term7=0.0001*(permE1(3,1,5,X,Y,Z,lamb)+permE2(3,1,5,X,Y,Z,lamb)-
                  permE3(3,1,5,X,Y,Z,lamb)-permE4(3,1,5,X,Y,Z,lamb)+
                  permO1(3,1,5,X,Y,Z,lamb)+permO2(3,1,5,X,Y,Z,lamb)-
                  permO3(3,1,5,X,Y,Z,lamb)-permO4(3,1,5,X,Y,Z,lamb))

    surf_eq = term1+term2+term3-term4-term5-term6+term7

    return surf_eq

def P_surf_eq(X,Y,Z, lamb):

    term1=(permE1(1,0,0,X,Y,Z,lamb))

    term2=0.2260*(permE1(1,0,0,X,Y,Z,lamb)+permO1(1,0,0,X,Y,Z,lamb))

    term3=0.0516*(permE1(1,1,1,X,Y,Z,lamb)+permO1(1,1,1,X,Y,Z,lamb))

    term4=0.0196*(permE1(2,1,0,X,Y,Z,lamb)+permO1(2,1,0,X,Y,Z,lamb))

    term5=0.0027*(permE1(3,0,0,X,Y,Z,lamb)+permO1(3,0,0,X,Y,Z,lamb))


    surf_eq = term1+term2-term3-term4-term5

    return surf_eq



def point_generator(l, surface, ncells):

    surfaces = {'D': {'eq': D_surf_eq,
                      'factor': 1},
                'P': {'eq': P_surf_eq,
                      'factor': 2},
                'G': {'eq': G_surf_eq,
                      'factor': 2},
                }

    # define the mgrid from which to generate the points
    # not sure why, but D generates an actual unit cell over the
    # 0:1l range in 3D, but P and G need 0:2l
    n = ncells * surfaces[surface]['factor']
    nj = 1j * ncells * surfaces[surface]['factor']
    grid = np.mgrid[
        slice(0, n * l, l * nj),
        slice(0, n * l, l * nj),
        slice(0, n * l, l * nj)
    ]

    X, Y, Z = grid

    lamb = 1 / l

    surf_eq = surfaces[surface]['eq'](X, Y, Z, lamb)

    #find vertices on the surface
    vertices, simplices,normals, values = measure.marching_cubes(surf_eq,
                                                                 # step_size = 10,
                                                                 allow_degenerate=False,
                                                                 )

    #sort out the vertices and append them to the list of coordinates to write to file
    Xp,Yp,Zp = zip(*vertices)

    surface_points = np.array([Xp,Yp,Zp]).T

    return surface_points, normals

#Function to read the arguments
def read_arguments():
    parser = argparse.ArgumentParser(description='Generate a .stl file of a TPMS of given size and symmetry')
    parser.add_argument("-l",type=int,help='Lattice parameter of cubic surface', required=True)
    parser.add_argument("-t",type=str,help='Topology of TPMS. Must be one of: "D" (Diamond), "G" (Gyroid), or "P" (Primitive)', required=True)
    parser.add_argument("-c",type=int,help='Number of unit cells to generate', required=True, default=1)
    parser.add_argument("-n",type=int, help='Number of triangles to output into the mesh', default = 200, required=False)
    parser.add_argument("-op",type=bool, help='Output points file for quick inspection', required=False)
    parser.add_argument("-os",type=str,help='Output stl file', required=False, default='mesh.stl')
    args = parser.parse_args()
    return args

def points_out(a):
    import MDAnalysis as mda

    u1 = mda.Universe.empty(n_atoms = a[::10].shape[0],
                            n_residues=1,
                            )

    u1.load_new(a[::10])

    dim = int(max(a[:, 0]) - min(a[:, 0]))
    u1.dimensions = [dim, dim, dim, 90, 90, 90]

    ag = u1.select_atoms('all')
    ag.write('points.gro')

def main():
    args = read_arguments()

    print(f'Will generate a {args.t} surface with lattice parameter {args.l}')
    print('generating points')
    b = point_generator(args.l, str(args.t))
    a = b[0][::1]

    if args.op == True:
        points_out(a)

    print('generating mesh')
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(a)
    pcd.normals = o3d.utility.Vector3dVector(b[1])

    bpa_mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)

    dec_mesh = bpa_mesh.simplify_quadric_decimation(args.n)

    dec_mesh.compute_triangle_normals()

    o3d.io.write_triangle_mesh(args.os, dec_mesh)
    print('all done!')

