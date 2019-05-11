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

data05 = pd.read_csv('data/task3-05V.csv', delimiter = ',')
f05 = np.array(data05['f'].tolist())
U05 = np.array(data05['U'].tolist())
# w1 = f1 * 2*np.pi
# ksi1 = (w1**2 - w0**2) / w1

data04l = pd.read_csv('data/task3-04Vl.csv', delimiter = ',')
f04l = np.array(data04l['f'].tolist())
U04l = np.array(data04l['U'].tolist())

data04h = pd.read_csv('data/task3-04Vh.csv', delimiter = ',')
f04h = np.array(data04h['f'].tolist())
U04h = np.array(data04h['U'].tolist())

data035l = pd.read_csv('data/task3-035Vl.csv', delimiter = ',')
f035l = np.array(data035l['f'].tolist())
U035l = np.array(data035l['U'].tolist())

data035h = pd.read_csv('data/task3-035Vh.csv', delimiter = ',')
f035h = np.array(data035h['f'].tolist())
U035h = np.array(data035h['U'].tolist())

data07 = pd.read_csv('data/task3-07V.csv', delimiter = ',')
f07 = np.array(data07['f'].tolist())
U07 = np.array(data07['U'].tolist())



# pp = np.polyfit(pz_I,pz_U,2)
# pf = np.poly1d(pp)
plt.figure(0)

# plt.plot(pz_I,pf(pz_I),'-',color = 'k')
# plt.errorbar(pz_I,pz_U,yerr = U_err,xerr =I_err  ,color = 'k',linestyle='',capsize = 2)
plt.plot(f07,U07,'s-',color = 'green',label = '$U_{out}=700 mV$')
plt.plot(f05,U05,'o-',color = 'red',label = '$U_{out}=500 mV$')
plt.plot(f04h,U04h,'o-',color = 'k',label = '$U_{out}=400 mV$')
plt.plot(f04l,U04l,'o-',color = 'k',)
plt.plot(f035h,U035h,'o--',color = 'b',label = '$U_{out}=350 mV$')
plt.plot(f035l,U035l,'o--',color = 'b')
plt.grid(which='minor', linestyle='-',color = 'lightgrey')
plt.grid(which='major', linestyle='-',color = 'black')
plt.ylabel('$U_{amp}, V$')
plt.xlabel('$f_{out}, kHz$')
plt.minorticks_on()
plt.legend()
# plt.savefig('graphs/soft1.png',dpi=500)

plt.show()
