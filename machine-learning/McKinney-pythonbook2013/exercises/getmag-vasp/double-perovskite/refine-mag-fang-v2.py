#Purpose: export the moments of selected atoms
#Author: Yue-Wen Fang
#Date: 27th September, 2017, NYU SHANGHAI
#pyinstaller -F *.py to generate the excutable binary file.
#Revision history:
#Date: 23th November, 2017, Kyoto University; output total magnetic moment of the selected ion
#Date: 2th December, 2017, Kyoto University; check if a file exsits
#Date: 3th December, 2017, Kyoto University; interactive with keyboard input, now we can select atoms through keyboard
import math
import os
from tempfile import TemporaryFile

path = 'mag-fang.out'

###################################################
# Check if a file exsits
if os.path.exists(path):
    print('Congratuations, mag-fang.out exists.\n')
else:
    print('No mag-fang.out, please use getmag-fang to generate it.\n')
###################################################


###################################################
# Input the atoms you are intested in, the number must be consistent to the POSCAR
NumberOfAtoms=input('Input the numbers of atoms in POSCAR, if there are several ions, please use comma: ')
print('\n')
#print(NumberOfAtoms)
#print(type(NumberOfAtoms))


NumberOfAtoms=NumberOfAtoms.split(",")

#print(type(NumberOfAtoms))
#print(NumberOfAtoms)

space='       ' 
# I add space here so that I can locate the number in the mag-fang.out file
###################################################


###################################################


# this is a temp variable for stroing the magnetic information

for ion in NumberOfAtoms:
    f = open(path, 'rt')
    print(ion)
    Store_Mag = [] 
    ion_with_space = ion + space
#    print(ion_with_space)
    for line in f:
        if ion_with_space in line:
            Line_String = str(line)
#            print(Line_String[33:40], sep=' ', end=' ')
            Store_Mag.append(Line_String[33:40])
#            print(Store_Mag)

    mag_x, mag_y, mag_z = Store_Mag[:]
    mag_x=float(mag_x)
    mag_y=float(mag_y)
    mag_z=float(mag_z)
    total_mag=math.sqrt(abs(mag_x)**2+abs(mag_y)**2+abs(mag_z)**2)
    print('...x....y....z....total')
    print(mag_x, mag_y, mag_z, total_mag)
    
    f.close
    print('\n')
