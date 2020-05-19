# 1. Fermi surface calculations

- [VESTA绘制六角倒空间布里渊区的费米面](http://blog.sciencenet.cn/blog-3352196-1069656.html)
  - [使用MATLAB将BXSF文件转换为可以用VESTA打开的XSF文件](<http://blog.sciencenet.cn/home.php?mod=space&uid=1502061&do=blog&id=1026133>)

- [Xcrysden: Visualization of Fermi surface](<http://www.xcrysden.org/doc/fermi.html>)

- [Convert POSCAR to XSF files](<http://home.ustc.edu.cn/~lipai/scripts/ml_scripts/pos2xsf.html>)

- [Generates a .bxsf (XCrysDen Fermi surface format) from VASP outputs](<https://github.com/bkchang/vasp2x_fs>)

- [[FermiSurfer: an visualization tool for Fermi surfaces ](http://osdn.jp/projects/fermisurfer/)]

# ２. 有效质量，能带图中k点坐标的单位

- [小木虫：于电子有效质量计算方法的问题](http://muchong.com/t-10575534-1)

- [小木虫：能带结果的横坐标单位](http://muchong.com/html/201708/7390503.html)

- [小木虫：一种计算电子和空穴有效质量的方法](http://muchong.com/t-7149817-1-amp;fpage-1)

# 3. Fat band or orbital projected band structure analysis 

- [Projected band with Pymatgen: pymatgen.electronic_structure.plotter](http://blog.wangruixing.cn/2019/05/19/pymatgen-band/)

  - [an example](https://kwaters4.github.io/journal/Projected_DOS.html)
- Sumo (sumo code, git grep 'BandStructureSymmLine')

# 4 Wannier-VASP and wannier90 calculations

- [Restarting the calculation with increased dis_num_iter](https://lists.quantum-espresso.org/pipermail/wannier/2014-December/000929.html): at present,
it is impossible to restart the disentanglement with increased dis_numb_inter;
but it's allowed to restart the wannierisation with increased num_iter, note
that the XX.chk file must be present so that the calculations can restart from
the checkpoint.

- [Restart the calculation of Fermi surface]: if we have finished the
  disentanglement and wannierization, we can use 'restart=plot' to calculate
the Fermi surface. Specifically, we need add these lines to the XX.win file:

  restart=plot

  fermi_energy = E_F-from-DFT

  fermi_surface_plot = true

  fermi_surface_num_points = 50
  
- [Wannier calculation convergence](https://lists.quantum-espresso.org/pipermail/wannier/2016-May/001171.html)

```
There are 4 criterion:
1.In the  output file you should see this:<<< Wannierisation
convergence criteria satisfied >>>
2.WF spread (for final state) should be < 5 angstrom
3. Maximum Im/Re Ratio should be < 10^-4
4. And finally comparing the band structures by wannier90 with DFT
```

# 5 PBEsol-D2 is currently not support at least in vasp 5.4.4.

In my recent study, I found that for PBEsol (GGA=PS in INCAR and LEXCH=PS in POTCAR), DFT-D2 ( IVDW = 10 in INCAR) doesn't work after finisihing an ionic step with the errors

" vdw_forces_G: ERROR unsupported xc-functional, LEXCH=          14
 please define parameter VDW_S6 for this functional"

# 6 Linear Response U by Dr. Eric B. Isaacs 

http://grandcentral.apam.columbia.edu:5555/tutorials/dft_procedures/linear_response_u/index.html

Dr. Isaacs is now a postdoc in the group of Wolverton (https://sites.northwestern.edu/ericisaacs/)