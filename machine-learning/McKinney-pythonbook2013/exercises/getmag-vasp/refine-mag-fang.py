#Purpose: export the moments of selected atoms
#Author: Yue-Wen Fang
#Date: 27th September, 2017
#pyinstaller -F *.py to generate the excutable binary file.
path = 'mag-fang.out'

f = open(path)
for line in f:
        if '13       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
f.close()

print('\n')

f = open(path)
for line in f:
        if '14       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
f.close()

print('\n')

f = open(path)
for line in f:
        if '15       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
f.close()
        
    
print('\n')

f = open(path)
for line in f:
        if '16       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
f.close()
print('\n')
