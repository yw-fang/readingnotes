# Common errors in VASP

- VERY BAD NEWS! internal error in subroutine SGRCON

This error is usually caused by the symmetry accuracy of structure. 
Some solutions include 1) including SYMPREC, 2) turn off symmetry by
ISYM = 1 or 0, 3) higher kpoints

- The isovalue of ELF in vesta is extremely low.

ELFCAR is generated by VASP, if we copy it to ABO3.vasp, and open ABO3.vasp
with VESTA, we will find the isovalue is only about 0.00X, this is not reasonable
because it's too small. I find that, if we copy it to ELFCAR.vasp, VESTA can then
read the isovalue in the right way.

- BRMIX: very serious problems the old and the new charge density differ changed to new machine

This error generally occur in the study of metallic materials. However, you may find that no matter whatever you modify in the INCAR, you will find it doesn't work. It's more likely to be an error if the VASP is compiled with the intel MPI. For example, as I used the NYU Shanghai cluster, I used these modules: module load icc/18.0.5; module load mkl/19.0.2; module load impi/18.0.5

This error frequently shows up. I have tried a lot of different ways, including recompiling with the -O1 tag (because some guys on the internet said it worked), modifying INCAR (ALGO, mixing parameter, etc). None of them worked! Until yesterday, I found the specilist in the LIU mentioned to add "export I_MPI_ADJUST_REDUCE=3" to the job script to sabilize the calculation.

The following paragraphs are from their [website](https://www.nsc.liu.se/software/installed/tetralith/vasp/):

f you encountered the problem `BRMIX: very serious problems the old and the new charge density differ` written in the slurm output, with VASP calculations on Tetralith / Sigma for cases which typically work on other clusters and worked on Triolith / Gamma, it might be related to bug/s which was traced back to `MPI_REDUCE` calls. These problems were transient, meaning that out of several identical jobs, some go through, while others fail. Our VASP modules are now updated to use another algorithm by setting `I_MPI_ADJUST_REDUCE=3`, which shouldn't affect the performance. If you don't load modules, but run binaries directly, set in the job script:

```
export I_MPI_ADJUST_REDUCE=3
```

More details for the interested: the problem was further traced down to our setting of the NB blocking factor for distribution of matrices to `NB=32` in `scala.F`. The VASP default of `NB=16` seems to work fine, while `NB=96` also worked fine on Triolith. By switching off ScaLAPACK in INCAR, `LSCALAPACK = .FALSE.` it also works. Furthermore, the problem didn't appear for gcc + OpenBLAS + OpenMPI builds.

Newer VASP modules built with e.g. `intel-2018b` use VASP default `NB=16`, while the non-vanilla modules built with `intel-2018a` has `NB=32` set.

- REAL_OPTLAY: internal error

  This error aries if the ENMAX values of the elements in the POTCAR differ very much, and can be solved by altering the POTCAR files. See ref: https://www.vasp.at/forum/viewtopic.php?f=4&t=5354