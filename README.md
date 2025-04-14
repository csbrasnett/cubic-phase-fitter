# cubic-phase-fitter

Library for generating and fitting triply periodic minimal surfaces. This project is under development. If you come
across an error, please open an [issue](https://github.com/csbrasnett/cubic-phase-fitter/issues)

## installation

Install the cubic-phase-fitter library in a virtual environment:

```commandline
python3 -m venv venv && source venv/bin/activate # Not required, but often convenient.
pip install git+https://github.com/csbrasnett/cubic-phase-fitter
```

## generating surfaces

Surface generation is done with the `cubicsurfacegen` program. The program will
generate an stl surface mesh, e.g:

```commandline
$ cubicsurfacegen -t D -os diamond.stl -l 100 -n 10000 -op true
```

will generate a Diamond surface with a lattice parameter of 100. The `-op` option is used to also output a `.gro` file 
for quick evaluation of the generation routine. The number of triangles the mesh can be tuned using the `-n` option,
which uses `open3d.geometry.simplify_quadric_decimation` to reduce the number from the initiall generated mesh.


## fitting surfaces

The `cubic-phase-fitter` library is principally designed to fit surfaces from molecular dynamics simulations 
using gromacs of cubic phase systems using the `cubicphasefitter` program. The functionality is currently limited 
to diamond cubic phases. 

### Default behaviour

The most trivial command to use is:

```commandline
$ cubicphasefitter -f trajectory.xtc -s topology.tpr 
```

will take the simulation described in the files and fit a Diamond surface to the atoms that match the default residue 
and atomnames: `MO` and `C4A` respectively. If you have simulated a cubic phase system using another lipid, the lipid 
residue name and its terminal tail bead names can be specified using the `-main-res` and `-main-atom` flags respectively.
The residuals of the fit are saved as a dictionary of time, values items in a pickle file called `residuals.p`.

### More unit cells

If you've simulated a system containing multiple unit cells of a cubic phase, the
`-ncells` argument can be used to increase the number of unit cells fitted.

### Visualising

To visualise the fitted frame, the `-write-frame` flag is used. In this case, the frame fitted is written as a `.gro` file
with its simulation time as its name. The fitted surface is written out as a collection of points in space, grouped by 
gaussian curvature so that they can be coloured accordingly. 





