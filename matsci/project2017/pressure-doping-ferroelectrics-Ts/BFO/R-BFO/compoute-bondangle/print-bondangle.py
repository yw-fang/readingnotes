from pymatgen.io.vasp import Poscar
from pymatgen import *
import ase
from ase.io import read, write
from numpy import pi
from ase import Atoms
from ase.structure import molecule

p = Poscar.from_file('POSCAR')

#atoms = read('POSCAR', index=0, format='vasp')
#cell=atoms.get_cell()
#print(cell.round(3))
#print('theta = {0} degrees'.format(atom))


#at = molecule('NH3')
#print('theta = {0} degrees'.format(at.get_angle([1,0,3])*180./pi))

print(p.structure.get_all_neighbors(3))
#print(type(p))