import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages

plt.rc('text', usetex = True)
plt.rc('font', size=13, family = 'serif')
# plt.rc('text.latex',unicode=True)
plt.rc('legend', fontsize=14)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')

f0 = 420.7
w0 = f0 * 2*np.pi
# mu = 
## Parazite Voltage

data1 = pd.read_csv('data/task1V.csv', delimiter = ',')
f1 = np.array(data1['f'].tolist())
U1 = np.array(data1['U'].tolist())
w1 = f1 * 2*np.pi
ksi1 = (w1**2 - w0**2) / w1

data13 = pd.read_csv('data/task13V.csv', delimiter = ',')
f13 = np.array(data13['f'].tolist())
U13 = np.array(data13['U'].tolist())
w13 = f13 * 2*np.pi
ksi13 = (w13**2 - w0**2) / w13

data06 = pd.read_csv('data/task06V.csv', delimiter = ',')
f06 = np.array(data06['f'].tolist())
U06 = np.array(data06['U'].tolist())
w06 = f06 * 2*np.pi
ksi06 = (w06**2 - w0**2) / w06

data03 = pd.read_csv('data/task03V.csv', delimiter = ',')
f03 = np.array(data03['f'].tolist())
U03 = np.array(data03['U'].tolist())
w03 = f03 * 2*np.pi
ksi03 = (w03**2 - w0**2) / w03

# pp = np.polyfit(pz_I,pz_U,2)
# pf = np.poly1d(pp)
plt.figure(0)

# plt.plot(pz_I,pf(pz_I),'-',color = 'k')
# plt.errorbar(pz_I,pz_U,yerr = U_err,xerr =I_err  ,color = 'k',linestyle='',capsize = 2)
plt.plot(f1,U1,'o-',color = 'red',label = '$U_{out}=1 V$')
plt.plot(f13,U13,'s-',color = 'green',label = '$U_{out}=1.3 V$')
plt.plot(f06,U06,'o-',color = 'k',label = '$U_{out}=0.6 V$')
plt.plot(f03,U03,'o--',color = 'b',label = '$U_{out}=0.3 V$')
plt.grid(which='minor', linestyle='-',color = 'lightgrey')
plt.grid(which='major', linestyle='-',color = 'black')
plt.ylabel('$U_{amp}, V$')
plt.xlabel('$f_{out}, kHz$')
plt.minorticks_on()
plt.legend()
# plt.savefig('graphs/soft1.png',dpi=500)

plt.show()
