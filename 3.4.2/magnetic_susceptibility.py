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

ar = open_file("magnetic_s_input.txt")

x = [] ; xErr = []; y = []; yErr = [];


for i in range(len(ar)):
    x.append(ar[i ][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])


xminorLocator = MultipleLocator(1)
yminorLocator = MultipleLocator(0.01)

xmajorLocator = MultipleLocator(5)
ymajorLocator = MultipleLocator(0.05)

ax = plt.subplot()


plt.plot(x, y, '.')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')



f = interp1d(x, y, kind=3)

x_spline = np.linspace(x[0], x[-1], 500)

plt.plot(x_spline,f(x_spline), 'g-.')




ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(14, 41)
plt.ylim(0, 0.5)

plt.title(u'')
plt.title(u"Магнитная восприимчивость Gd "+r"$\chi(T)$")
plt.xlabel(u'$T, ^0C$')
plt.ylabel(r'$\chi(T)$')


plt.show()