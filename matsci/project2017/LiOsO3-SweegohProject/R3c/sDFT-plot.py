%matplotlib inline

# For the reference of the default color map of matplotlib, see
# https://matplotlib.org/users/dflt_style_changes.html

# This example is from CHAPTER 3 of the book "
# matplotlib for developpers",
# but I made many revisions

import matplotlib.style
import matplotlib as mpl
mpl.style.use('classic')
mpl.rcParams['figure.facecolor'] = '1'
#if choose the grey backgroud, use 0.75
mpl.rcParams['figure.figsize'] = [8,13]
mpl.rcParams['lines.linewidth'] = 1.5
mpl.rcParams['legend.fancybox'] = True
mpl.rcParams['legend.framealpha'] = 0.8
mpl.rcParams['legend.fontsize'] = 17
mpl.rcParams['legend.scatterpoints'] = 1 #scatterpoints,
#it's the numer of maker points in the legend when
#creating a legend entry for a scatter plot
mpl.rcParams["axes.formatter.useoffset"]=False #turn off the axis offset-values. 
# If on. the axis label will use a offset value by the side of axis
mpl.rcParams["axes.linewidth"]  = 1.5 #change the boarder width
#plt.rcParams["axes.edgecolor"] = "0.15" #change the boarder color

ticklabel_size = 19
mpl.rcParams['xtick.labelsize'] = ticklabel_size
mpl.rcParams['ytick.labelsize'] = ticklabel_size


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#import pdf module
from matplotlib.backends.backend_pdf import PdfPages


#R_3c_PV = pd.read_csv('./sDFT-SOC-U-verification/R-3c-AFM-PV.dat', header=None, delim_whitespace=True)
#R_3c_toten=pd.read_csv('./sDFT-SOC-U-verification/R-3c-AFM-toten.dat', header=None, delim_whitespace=True)
R_3c_enthalpy = pd.read_csv('./sDFT-SOC-U-verification/R-3c-AFM-enthalpy.dat', header=None, delim_whitespace=True)
#R3c_PV=pd.read_csv('./sDFT-SOC-U-verification/R3c-AFM-PV.dat', header=None, delim_whitespace=True)
#R3c_toten=pd.read_csv('./sDFT-SOC-U-verification/R3c-AFM-toten.dat', header=None, delim_whitespace=True)
R3c_enthalpy = pd.read_csv('./sDFT-SOC-U-verification/R3c-AFM-enthalpy.dat', header=None, delim_whitespace=True)
#Imma_PV=pd.read_csv('./sDFT-SOC-U-verification/Imma-AFM-PV.dat', header=None, delim_whitespace=True)
#Imma_toten=pd.read_csv('./sDFT-SOC-U-verification/Imma-AFM-toten.dat', header=None, delim_whitespace=True)
Imma_enthalpy = pd.read_csv('./sDFT-SOC-U-verification/Imma-AFM-enthalpy.dat', header=None, delim_whitespace=True)
#Pbnm_PV=pd.read_csv('./sDFT-SOC-U-verification/Pbnm-AFM-PV.dat', header=None, delim_whitespace=True)
#Pbnm_toten=pd.read_csv('./sDFT-SOC-U-verification/Pbnm-AFM-toten.dat', header=None, delim_whitespace=True)
#Pbnm_enthalpy = pd.read_csv('./sDFT-SOC-U-verification/Pbnm-AFM-enthalpy.dat', header=None, delim_whitespace=True)
#Pnma_PV=pd.read_csv('./sDFT-SOC-U-verification/Pnma-AFM-PV.dat', header=None, delim_whitespace=True)
#Pnma_toten=pd.read_csv('./sDFT-SOC-U-verification/Pnma-AFM-toten.dat', header=None, delim_whitespace=True)
Pnma_enthalpy = pd.read_csv('./sDFT-SOC-U-verification/Pnma-AFM-enthalpy.dat', header=None, delim_whitespace=True)

fig1 = plt.figure()
ax1_1=fig1.add_subplot(3,1,1)
ax1_1.plot(R_3c_enthalpy[0]/10, R_3c_enthalpy[1]/2-R3c_enthalpy[1]/2, 'ro-', markersize=10, label = r'${R\bar{3}c}$') 
#ax1_1.plot(R3c_enthalpy[0], R3c_enthalpy[1]/2, 'bo-', markersize=10, label = 'R3c') 
ax1_1.plot(Imma_enthalpy[0]/10, Imma_enthalpy[1]/4-R3c_enthalpy[1]/2, 'bo-', markersize=10, label = '${Imma}$') 
ax1_1.plot(Pbnm_enthalpy[0]/10, Pbnm_enthalpy[1]/4-R3c_enthalpy[1]/2, 'go-', markersize=10, label = '${Pbnm}$') 
#ax1_1.plot(Pnma_enthalpy[0]/10, Pnma_enthalpy[1]/4-R3c_enthalpy[1]/2, 'yo-', markersize=10, label = 'Pnma') 

ax1_1.legend(loc="best")
ax1_1.text(-2.5, 0.25, '(a)', fontsize=22)
#plt.xticks(x, SpinConfLabel, rotation='270')
plt.setp(ax1_1.get_xticklabels(), visible=True)
#ax1_1.set_xlabel('Pressure (GPa)',fontsize=22)
ax1_1.set_ylabel('$\Delta H$ (eV/f.u.)',fontsize=22)
ax1_1.locator_params(nbins=5, axis='y')
ax1_1.grid()
#ax1_1.axhline(y=0, color='orange', linestyle='-')
ax1_1.set_xlim([0.0,12.0]) #set x-axis limit
#ax1_1.set_ylim([0.0,7.0]) #set x-axis limit
#plt.axvline(x=0.0, color='orange', linestyle='--') #add a vertical line
plt.tight_layout()


# ax1_2=fig1.add_subplot(3,1,2)
# ax1_2.text(-2.5, 0.1, '(b)', fontsize=22)
# ax1_2.plot(R_3c_PV[0]/10, R_3c_PV[1]/2-R3c_PV[1]/2, 'ro-', markersize=10, label = ' ') 
# #ax1_2.plot(R3c_PV[0], R3c_PV[1]/2, 'bo-', markersize=10, label = 'R3c') 
# ax1_2.plot(Imma_PV[0]/10, Imma_PV[1]/4-R3c_PV[1]/2, 'bo-', markersize=10, label = ' ') 
# ax1_2.plot(Pbnm_PV[0]/10, Pbnm_PV[1]/4-R3c_PV[1]/2, 'go-', markersize=10, label = ' ') 
# #ax1_2.plot(Pnma_PV[0]/10, Pnma_PV[1]/4-R3c_PV[1]/2, 'yo-', markersize=10, label = 'Pnma') 

# #ax1_2.legend(loc="best")
# plt.setp(ax1_2.get_xticklabels(), visible=True)
# #ax1_2.set_xlabel('Pressure (GPa)',fontsize=22)
# ax1_2.set_ylabel('$P \Delta V$ (eV/f.u.)',fontsize=22)
# ax1_2.locator_params(nbins=5, axis='y')
# ax1_2.grid()
# ax1_2.set_xlim([0.0,12.0]) #set x-axis limit
# plt.tight_layout()

# ax1_3=fig1.add_subplot(3,1,3)
# ax1_3.text(-2.5, 0.2, '(c)', fontsize=22)
# ax1_3.plot(R_3c_toten[0]/10, R_3c_toten[1]/2-R3c_toten[1]/2, 'ro-', markersize=10, label = ' ') 
# #ax1_3.plot(R3c_toten[0], R3c_toten[1]/2, 'bo-', markersize=10, label = 'R3c') 
# ax1_3.plot(Imma_toten[0]/10, Imma_toten[1]/4-R3c_toten[1]/2, 'bo-', markersize=10, label = ' ') 
# ax1_3.plot(Pbnm_toten[0]/10, Pbnm_toten[1]/4-R3c_toten[1]/2, 'go-', markersize=10, label = ' ') 
# #ax1_3.plot(Pnma_toten[0]/10, Pnma_toten[1]/4-R3c_toten[1]/2, 'yo-', markersize=10, label = 'Pnma') 

# #ax1_3.legend(loc="center left")
# plt.setp(ax1_3.get_xticklabels(), visible=True)
# ax1_3.set_xlabel('$P$ (GPa)',fontsize=22)
# ax1_3.set_ylabel('$\Delta E$ (eV/f.u.)',fontsize=22)
# ax1_3.locator_params(nbins=5, axis='y')
# ax1_3.grid()
# ax1_3.set_xlim([0.0,12.0]) #set x-axis limit
# plt.tight_layout()


pp1 = PdfPages('./enthalpy-sDFT.pdf')
pp1.savefig(fig1)
pp1.close()
