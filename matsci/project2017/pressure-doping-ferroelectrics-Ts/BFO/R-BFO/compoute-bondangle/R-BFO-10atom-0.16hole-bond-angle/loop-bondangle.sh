#!/bin/bash

for((i=0;i<=120;i=i+20));
#for((i=85;i<=95;i=i+5));
#for((i=200;i<=800;i=i+100));
do
cp ../$i/CONTCAR ./POSCAR-$i.vasp
done


#for((i=0;i<=120;i=i+20));
#for((i=200;i<=800;i=i+100));
#do
#cp ../$i/scf/POSCAR ./POSCAR-$i.vasp
#done
