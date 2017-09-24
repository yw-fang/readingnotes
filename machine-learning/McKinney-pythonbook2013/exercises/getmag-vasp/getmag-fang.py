import numpy as np

file1 = open('OUTCAR')
I = file1.readline()
for i in I:
    if 'TOTEN' in i:
        print('OK')
file1.close()
