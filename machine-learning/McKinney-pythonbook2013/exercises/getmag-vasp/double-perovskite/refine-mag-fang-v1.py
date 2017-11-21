path = 'mag-fang.out'
path1 = 'temp.dat'

f = open(path)
f1 = open(path1,'w')
for line in f:
        if '13       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
            f1.write(a[33:40])
#b = [a[33:40]]
#print(b)

f.close()
f1.close()
print('\n')
path = 'totalmag.out'
f1=open(path1)
for line in f1:
    a=[line]
print(a)

print('\n')
