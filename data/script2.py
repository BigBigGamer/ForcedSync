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

data1 = pd.read_csv('data/task2.csv', delimiter = ',')
U1 = np.array(data1['U'].tolist())
cl = np.array(data1['cl'].tolist())
hl = np.array(data1['hl'].tolist())
cr = np.array(data1['cr'].tolist())
hr = np.array(data1['hr'].tolist())
ca = np.array(data1['ca'].tolist())
ha = np.array(data1['ha'].tolist())
# w1 = f1 * 2*np.pi
# ksi1 = (w1**2 - w0**2) / w1

# pp = np.polyfit(pz_I,pz_U,2)
# pf = np.poly1d(pp)
plt.figure(0)

# plt.plot(pz_I,pf(pz_I),'-',color = 'k')
# plt.errorbar(pz_I,pz_U,yerr = U_err,xerr =I_err  ,color = 'k',linestyle='',capsize = 2)

# plt.plot(cl,U1,'o--',color = 'red',label = 'Захват')
# plt.plot(cr,U1,'o--',color = 'red')
# plt.plot(hl,U1,'.-',color = 'k',label = 'Удержание')
# plt.plot(hr,U1,'.-',color = 'k')

plt.plot(U1,ha,'s-',color = 'k',label = 'Удержание')
plt.plot(U1,ca,'.-',color = 'r',label = 'Захват')

plt.grid(which='minor', linestyle='-',color = 'lightgrey')
plt.grid(which='major', linestyle='-',color = 'black')
plt.ylabel('$U_{amp}, mV$')
plt.xlabel('$U_{out}, mV$')
# plt.xlabel('$f_{out}, kHz$')
plt.minorticks_on()
plt.legend()
# plt.savefig('graphs/amps.png',dpi=500)

plt.show()
