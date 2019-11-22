# The current tools for Bands unfolding interfaced to VASP

- [**BandUP**](http://www.ifm.liu.se/theomod/compphys/band-unfolding/): Band Unfolding code for Plane-wave based calculations

BandUP is a code that allows you to obtain a primitive cell representation of the band structure of systems simulated using supercells. The unfolding of the bands is performed as described in the following papers: *Phys.Rev. B* 89, 041407(R) (2014); *Phys.Rev. B* 91, 041116(R) (2015).

https://github.com/band-unfolding/bandup

- [**vasp_unfold**](https://github.com/tomkeus/vasp_unfold): Bandstructure unfolding for VASP

vasp_unfold works as a postprocessing tool. The unfolding is achieved through manipulation of orbital weights. Basically, in the unfolded bandstructure, orbital weights of some bands are set to zero. This means that the effect of unfolding can only be seen with the fatband plots. In order for vasp_unfold to be able to work, the phase information must be present in the PROCAR file which means that LORBIT=12 must be set in the INCAR file. *Phys. Rev. B* 90, 195121 (2014).

https://github.com/tomkeus/vasp_unfold

- [**KPROJ**](https://mingxingchen.weebly.com/kproj.html): A band unfolding code

KPROJ, based on thek-projection method, is a code to perform band unfolding using supercell calculations. It is designed for the investigation of effects of doping, structural reconstruction/distortion on the band structure of host materials. It is ideal for interfaces and heterostructures, in which the two constituents have different supercells. Currently, it is interfaced to VASP.

https://mingxingchen.weebly.com/kproj.html

- [**Band Unfolding**](https://github.com/QijingZheng/VaspBandUnfolding)

Using the pseudo-wavefunction from supercell calculation, it is possible to perform electronic band structure unfolding to obtain the effective band structure. For more information, please refer to the following article and the GPAW website. *Phys. Rev. B* 85, 085201 (2012).

https://github.com/QijingZheng/VaspBandUnfolding

- [**Quantum Unfolding**](http://cpc.cs.qub.ac.uk/summaries/AEVF_v1_0.html): A program for unfolding electronic energy bands of materials

The electron wavefunction is reconstructed from Wannier functions and Hamiltonian parameters, which are produced by Wannier90 package. Then by using fast Fourier transformation (FFT), we get the Fourier components of the reconstructed wavefunction. The unfolding weight is calculated from the Fourier components, based on group theory and its special form for plane-wave basis. *Comput. Phys. Commun.* 189, (2015), 213.

http://cpc.cs.qub.ac.uk/summaries/AEVF_v1_0.html

- [**fold2Bloch-Wien2k**](https://github.com/rubel75/fold2Bloch-Wien2k/wiki): Unfolding of first-principle electronic band structure

Unfolding of first-principle electronic band structure obtained with WIEN2k DFT-(L)APW code.

*Phys. Rev. B* 90, 115202 (2014); [Phys. Rev. Lett. **104**, 236403 (2010)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.104.236403); [Phys. Rev. Materials **2**, 114604](https://doi.org/10.1103/PhysRevMaterials.2.114604)

- [**fold2Bloch-VASP**](https://github.com/rubel75/fold2Bloch-VASP)

The fold2Bloch utility is designed to unfold the band structure of a supercell obtained with theVienna Ab initio Simulation Package (VASP) and compute an effective bandstructure in a primitive representation. It facilitates interpretation of large-scale electronic structure calculations, where the Bloch character of electronic eigenstates is perturbed by a disorder (defects, alloy elements,etc). Reading of wavefunctions is adapted from the WaveTrans code. 

*Phys. Rev. B* 90, 115202 (2014); [Phys. Rev. Lett. **104**, 236403 (2010)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.104.236403); [Phys. Rev. Materials **2**, 114604](https://doi.org/10.1103/PhysRevMaterials.2.114604)

https://github.com/rubel75/fold2Bloch-VASP