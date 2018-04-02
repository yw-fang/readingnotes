## A basic workflow of computing thermal conductivity using phono3py (2018 March)

1. Create POSCARs with displacements

phono3py -d --dim="2 2 2" -c POSCAR-unitcell

2. vasp calculations for these these POSCARs.

3. collect vasprun.xml and create FORCES_FC3

phono3py --cf3 disp-{00001..00111}/vasprun.xml

4. create fc2.hdf and fc3.hdf

phono3py --dim="2 2 2" --sym-fc -c POSCAR-unitcell

Here, --sym-fc is an alias to set both of --sym-fc2 and --sym-fc3r


5. thermal conductivity calculations 

5.1. using mesh 11*11*11

phono3py --dim="2 2 2" --pa="0 1/2 1/2 1/2 0 1/2 1/2 1/2 0" -c POSCAR-unitcell --mesh="11 11 11" --fc3 --fc2 --br

5.2. using mesh 19*1*19

phono3py --dim="2 2 2" --pa="0 1/2 1/2 1/2 0 1/2 1/2 1/2 0" -c POSCAR-unitcell --mesh="19 19 19" --fc3 --fc2 --br

6. extract data

phono3py-kaccum --mesh="19 19 19" --pa="0 1/2 1/2 1/2 0 1/2 1/2 1/2 0" POSCAR-unitcell kappa-m191919.hdf5 --temperature 300 |tee kaccum.dat

