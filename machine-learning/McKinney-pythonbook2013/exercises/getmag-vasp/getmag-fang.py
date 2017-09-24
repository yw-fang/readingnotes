import numpy as np

path = './OUTCAR'
path2 = 'mag-fang.out'

f = open(path)

linenumber = 0
for line in  f:
    linenumber = linenumber + 1
    if 'magnetization (x)' in line:
        #print(line)
        linenumber_mag = linenumber
f.close()

#print(linenumber_mag)

f = open(path)

f2 = open(path2,'w')
linenumber = 0

for line in f:
    linenumber = linenumber + 1
    if linenumber >= linenumber_mag:
        f2.write(line)
#        with open('mag-fang.out', 'w') as handle:
#            handle.writelines(line)
        print(line)
        if 'BZINTS' in line:
            break
    else:
        continue

f2.close()
f.close()
