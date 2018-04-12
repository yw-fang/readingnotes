from pymatgen.io.vasp import Poscar
from pymatgen import *
from numpy import pi
from numpy import arccos, dot, pi
from numpy.linalg import norm

yourfile = input('Choose a file: ')
p = Poscar.from_file(yourfile)


Fe_sum = (p.structure.frac_coords[8][2] + p.structure.frac_coords[9][2] +
          p.structure.frac_coords[10][2] + p.structure.frac_coords[11][2]
          + p.structure.frac_coords[12][2] + p.structure.frac_coords[13][2]
          + p.structure.frac_coords[14][2] + p.structure.frac_coords[15][2])/8
print(Fe_sum)
O_sum = (p.structure.frac_coords[16][2]+p.structure.frac_coords[18][2]
            +p.structure.frac_coords[24][2]+p.structure.frac_coords[26][2]
            +p.structure.frac_coords[20][2]+p.structure.frac_coords[22][2]
            +p.structure.frac_coords[28][2]+p.structure.frac_coords[30][2]
            +p.structure.frac_coords[17][2]+p.structure.frac_coords[19][2]
            +p.structure.frac_coords[25][2]+p.structure.frac_coords[27][2]
            +p.structure.frac_coords[23][2]+p.structure.frac_coords[21][2]
            +p.structure.frac_coords[29][2]+p.structure.frac_coords[31][2])/16
print(O_sum)

disp_frac = O_sum - Fe_sum
out_of_plane_latticeconstant = p.structure.lattice.c
disp = disp_frac*out_of_plane_latticeconstant
print('displacement  ($\AA$): ', disp)
# a = Fe1 - O1_Fe
# b = Fe1 - O2_Fe


# theta_rad = arccos(dot(a,b)/(norm(a)*norm(b)))  #in radians
# #print(theta_rad)
# theta_deg = theta_rad*180./pi
# print(theta_deg)
