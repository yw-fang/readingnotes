import random
import itertools as iter
import pymatgen as mg
import numpy as np
import math
from pymatgen.io.vasp import Poscar #ywfang
#ref:
#https://stackoverflow.com/questions/42179261/how-to-get-all-bond-angles-within-a-structure-using-pymatgen


def all_angles(POSCAR,amin,amax):

    s = mg.Structure.from_file(POSCAR)

    atoms = s.atomic_numbers

    van = [x for x in atoms if x == 23]
    length = len(van)
    nb = ['NONE']*length

    x = 0
    n = 0

    while x < length:

        nb[x] = s.get_neighbors(s[x],2.4)
        x += 1

    w = 100
    h = len(van)
    oxygen = [[0 for x in range(w)] for y in range(h)]

    x = 0
    y = 0

    while x < len(nb):

        y = 0
        n = 0

        while y < len(nb[x]):

            oxygen[x][n] = (nb[x][y][0]).coords
            n += 1
            y += 1

        x += 1

    x = 0

    while x < len(oxygen):
        oxygen[x] = [n for n in oxygen[x] if not isinstance(n,int)]
        x += 1

    van = [x for x in range(0,len(van))]

    x = 0
    while x < len(van):
        van[x] = s[van[x]].coords
        x += 1

    van = [np.array(x) for x in van]

    x = 0
    while x < len(van):

        oxygen[x] = [np.subtract(oxygen[x][y],van[x]) for y in range(0,len(oxygen[x]))]
        x += 1

    combo = [[0 for x in range(0,1000)] for y in range(0,len(van))]

    r = 0

    while r < len(van):
        x = 0
        for subset in iter.combinations(oxygen[r],2):
            combo[r][x] = subset
            x += 1
        r += 1

    x = 0
    while x < len(combo):
        combo[x] = [c for c in combo[x] if c != 0]
        x += 1


    angles =  [[0 for x in range(0,1000)] for y in range(0,len(van))]

    x = 0

    while x < len(combo):

        group = combo[x]

        y = 0

        while y < len(group):
            angles[x][y] = math.degrees(math.acos(np.dot(group[y][0],group[y][1])/(np.linalg.norm(group[y][0])*np.linalg.norm(group[y][1]))))
            y += 1

        angles[x] = [round(n,3) for n in angles[x] if n != 0 and n > amin and n < amax]

        x += 1

    angles = np.concatenate(angles,axis=0)

    return angles

all_angles('POSCAR',1,6)
#str=Poscar.from_file('POSCAR')
#print(all_angles(str, 1 ,6))