# Common errors in VASP

- VERY BAD NEWS! internal error in subroutine SGRCON

This error is usually caused by the symmetry accuracy of structure. 
Some solutions include 1) including SYMPREC, 2) turn off symmetry by
ISYM = 1 or 0, 3) higher kpoints
