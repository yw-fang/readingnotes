from pymatgen.io.vasp import Poscar
from pymatgen import *
from numpy import pi
from numpy import arccos, dot, pi
from numpy.linalg import norm

yourfile = input('Choose a file: ')
p = Poscar.from_file(yourfile)


Fe1 = p.structure.frac_coords[2]
print(Fe1)
O1_Fe = p.structure.frac_coords[9]
print(O1_Fe)
O2_Fe = p.structure.frac_coords[8]
print(O2_Fe)
a = Fe1 - O1_Fe
b = Fe1 - O2_Fe


theta_rad = arccos(dot(a,b)/(norm(a)*norm(b)))  #in radians
#print(theta_rad)
theta_deg = theta_rad*180./pi
print(theta_deg)
