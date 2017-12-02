#Purpose: export the moments of selected atoms
#Author: Yue-Wen Fang
#Date: 27th September, 2017, NYU SHANGHAI
#pyinstaller -F *.py to generate the excutable binary file.
#Revision history:
#Date: 23th November, 2017, Kyoto University; output total magnetic moment of the selected ion
import math
path = 'mag-fang.out'
path1 = 'temp.dat'


######*****for the first ion (number 13)
f = open(path)
f1 = open(path1,'w')
for line in f:
        if '13       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
            f1.write(a[33:40])          
f.close()
f1.close()
print('\n')

with open(path1) as f1:
    lis=[list(map(float,x.split()))  for x in f1 if x.strip()]
#print(lis)
##############################
#ref: https://stackoverflow.com/questions/12271503/python-read-numbers-from-text-file-and-put-into-list
# if x.strip() to skip blank lines
#use list(map(int,x.split()))  in case of python 3.x
#use map(int,x.split())  in case of python 2.x
##############################
#the usage of map
#map(int,'1 2 3 4'.split())
############################


lis1=[]
if len(lis1)==0:
    print('I created an empty list called lis1 ')
for i in [0,1,2]:
    lis1.append(abs(lis[0][i]))
    #([lis[0][i]])
print('lis1 prsents the absolute values of x_mag y_mag z_mag')
print(lis1[:])
total_mag_1=math.sqrt(lis1[0]**2+lis1[1]**2+lis1[2]**2)
print('the total magnetic moment is')
print(total_mag_1)

print('\n')






######*****for the first ion (number 14)
f = open(path)
f1 = open(path1,'w')
for line in f:
        if '14       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
            f1.write(a[33:40])          
f.close()
f1.close()
print('\n')

with open(path1) as f1:
    lis=[list(map(float,x.split()))  for x in f1 if x.strip()]
#print(lis)
##############################
#ref: https://stackoverflow.com/questions/12271503/python-read-numbers-from-text-file-and-put-into-list
# if x.strip() to skip blank lines
#use list(map(int,x.split()))  in case of python 3.x
#use map(int,x.split())  in case of python 2.x
##############################
#the usage of map
#map(int,'1 2 3 4'.split())
############################


lis1=[]
if len(lis1)==0:
    print('I created an empty list called lis1 ')
for i in [0,1,2]:
    lis1.append(abs(lis[0][i]))
    #([lis[0][i]])
print('lis1 prsents the absolute values of x_mag y_mag z_mag')
print(lis1[:])
total_mag_1=math.sqrt(lis1[0]**2+lis1[1]**2+lis1[2]**2)
print('the total magnetic moment is')
print(total_mag_1)

print('\n')






######*****for the first ion (number 15)
f = open(path)
f1 = open(path1,'w')
for line in f:
        if '15       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
            f1.write(a[33:40])          
f.close()
f1.close()
print('\n')

with open(path1) as f1:
    lis=[list(map(float,x.split()))  for x in f1 if x.strip()]
#print(lis)
##############################
#ref: https://stackoverflow.com/questions/12271503/python-read-numbers-from-text-file-and-put-into-list
# if x.strip() to skip blank lines
#use list(map(int,x.split()))  in case of python 3.x
#use map(int,x.split())  in case of python 2.x
##############################
#the usage of map
#map(int,'1 2 3 4'.split())
############################


lis1=[]
if len(lis1)==0:
    print('I created an empty list called lis1 ')
for i in [0,1,2]:
    lis1.append(abs(lis[0][i]))
    #([lis[0][i]])
print('lis1 prsents the absolute values of x_mag y_mag z_mag')
print(lis1[:])
total_mag_1=math.sqrt(lis1[0]**2+lis1[1]**2+lis1[2]**2)
print('the total magnetic moment is')
print(total_mag_1)

print('\n')






######*****for the first ion (number 16)
f = open(path)
f1 = open(path1,'w')
for line in f:
        if '16       ' in line:
            a = str(line)
            print(a[33:40], sep=' ', end=' ')
            f1.write(a[33:40])          
f.close()
f1.close()
print('\n')

with open(path1) as f1:
    lis=[list(map(float,x.split()))  for x in f1 if x.strip()]
#print(lis)
##############################
#ref: https://stackoverflow.com/questions/12271503/python-read-numbers-from-text-file-and-put-into-list
# if x.strip() to skip blank lines
#use list(map(int,x.split()))  in case of python 3.x
#use map(int,x.split())  in case of python 2.x
##############################
#the usage of map
#map(int,'1 2 3 4'.split())
############################


lis1=[]
if len(lis1)==0:
    print('I created an empty list called lis1 ')
for i in [0,1,2]:
    lis1.append(abs(lis[0][i]))
    #([lis[0][i]])
print('lis1 prsents the absolute values of x_mag y_mag z_mag')
print(lis1[:])
total_mag_1=math.sqrt(lis1[0]**2+lis1[1]**2+lis1[2]**2)
print('the total magnetic moment is')
print(total_mag_1)

print('\n')
