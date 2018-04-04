from pymatgen.io.vasp import Poscar
# from pymatgen import *
from numpy import pi
from numpy import arccos, dot  # pi
from numpy.linalg import norm
import numpy as np

yourfile = input('Choose a file: ')
p = Poscar.from_file(yourfile)

Os_frac_coord = p.structure.frac_coords[6:12]
# print(Os_frac_coord)
# print('\n')
aa = Os_frac_coord
Os_frac_coord_sort = aa[aa[:,2].argsort()]
print(Os_frac_coord_sort)

high_symmetry_array = np.array([[0.0,0.0,0],
                               [1.0/3, 2.0/3, 1./6],
                               [2./3, 1./3, 1./3],
                               [0.0, 0.0, 0.5],
                               [1.0/3, 2.0/3, 2.0/3],
                               [2.0/3, 1./3, 5./6]])


lattice_vector_H = p.structure.lattice.matrix
#Here, H is hexagonal
lattice_c_hexagonal = lattice_vector_H[2][2]
print('lattice constant $c$ of hexagonal lattice is ', lattice_c_hexagonal)

relative_disp_frac = np.subtract(Os_frac_coord_sort, high_symmetry_array)
relative_disp_cart = relative_disp_frac*lattice_c_hexagonal
# print(relative_disp_frac)
# print('\n')
# print(relative_disp_cart)

sum_disp_Os = np.absolute(relative_disp_cart).sum(1).sum(0)
print('sum of disp of all Os:', sum_disp_Os, ' angstrom')
average_disp_Os = sum_disp_Os/6.
print('average_disp_Os is', average_disp_Os)
# print(relative_disp_cart,' angstrom')
