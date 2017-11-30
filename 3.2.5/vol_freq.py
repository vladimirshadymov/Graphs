import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import interp1d


def open_file(path):
    input = open(path, 'r', encoding='utf-8')
    lines = input.readlines()
    lines_ = []
    for i in range(len(lines)):
        if lines[i] != '\n':
            lines_.append(lines[i])
    lines = lines_
    for i in range(len(lines)):
        lines[i] = [float(x) for x in lines[i].split()]
    return lines
ar = open_file("vol_freq.txt")

x = []; xErr = []; y = []; yErr = []

for i in range(len(ar)):
    x.append(ar[i ][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])

x_R0 = x[:14]
xErr_R0 = xErr[:14]
y_R0 = y[:14]
yErr_R0 = yErr[:14]


x_R100 = x[14:]
xErr_R100 = xErr[14:]
y_R100 = y[14:]
yErr_R100 = yErr[14:]




xminorLocator = MultipleLocator(0.02)
yminorLocator = MultipleLocator(0.02)

xmajorLocator = MultipleLocator(0.1)
ymajorLocator = MultipleLocator(0.1)

ax = plt.subplot()

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

ax.text(1.25, 0.45, r'$\nu_0$'+u' - резонансная частота'+'\n'+r'$U_0$'+u' - напряжение при'+'\n''резонансной частоте '+r'$\nu_0$', size='small', style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})

plt.plot(x, y, '.', color='k', label="Экспериментальные точки")
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')


resonance_R0 = interp1d(x_R0, y_R0, kind='cubic')
resonance_R100 = interp1d(x_R100, y_R100, kind='cubic')

xnew_R0 = np.linspace(x_R0[0], x_R0[len(x_R0)-1], num=5000)
xnew_R100 = np.linspace(x_R100[0], x_R100[len(x_R100)-1], num=5000)
plt.plot(xnew_R0, resonance_R0(xnew_R0), '-', label="R=0 Ом")
plt.plot(xnew_R100, resonance_R100(xnew_R100), '--', label="R=100 Ом")


"""
тут все и начинается
"""
U = resonance_R100(xnew_R100)
dU_dR = np.zeros(U.shape, np.float)

dU_dR[0:-1] = np.diff(U)/np.diff(xnew_R100) #матан как он есть

plt.plot(xnew_R100[0:-1], dU_dR[0:-1]/100, label = "Производная амплитуды напряжения \nпо частоте, уменьшенная в 100 раз")




plank_x = np.linspace(0.85, 1.2, num=500)
plank_y = [1/2**0.5]*500

plt.plot(plank_x, plank_y, linestyle = ':', color='red', linewidth=0.7)

plt.xlim(0.8, 1.4)
plt.ylim(-0.2, 1.05)
plt.title(u"Резонансные кривые вынужденных колебаний")
plt.xlabel(r'$\frac{\mathit{\nu}}{\mathit{\nu_0}}$', size='x-large')
plt.ylabel(r'$\frac{\mathit{U}}{\mathit{U_0}}$', size='x-large')
plt.legend(loc='best')

plt.show()
