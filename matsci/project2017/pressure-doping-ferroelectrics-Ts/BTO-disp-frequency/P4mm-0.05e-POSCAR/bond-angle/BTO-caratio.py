from pymatgen.io.vasp import Poscar
# from pymatgen import *
from numpy import pi
from numpy import arccos, dot  # pi
from numpy.linalg import norm
import numpy as np

yourfile = input('Choose a file: ')
p = Poscar.from_file(yourfile)


# Fe1 = p.structure.frac_coords[2]
# print(Fe1)
# O1_Fe = p.structure.frac_coords[9]
# print(O1_Fe)
# O2_Fe = p.structure.frac_coords[8]
# print(O2_Fe)
# a = Fe1 - O1_Fe
# b = Fe1 - O2_Fe
#
#
# theta_rad = arccos(dot(a,b)/(norm(a)*norm(b)))  #in radians
# #print(theta_rad)
# theta_deg = theta_rad*180./pi
# print(theta_deg)

lattice_vector_R = p.structure.lattice.matrix
print(lattice_vector_R)
lattice_a = lattice_vector_R[0][0]
lattice_c = lattice_vector_R[2][2]
ca_ratio = lattice_c/lattice_a
# print(lattice_a)
# print(lattice_c)
print(ca_ratio)

# high_symmetry= np.array([0.5, 0.5, 0.5])
# relative_disp_frac = Fe1-high_symmetry[0]
# relative_disp_cart = relative_disp_frac[1]*lattice_c_hexagonal
# print(relative_disp_cart,' angstrom')
