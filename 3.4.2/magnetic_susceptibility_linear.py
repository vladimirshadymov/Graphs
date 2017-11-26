import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy import stats

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

ar = open_file("magnetic_s_lin_input.txt")

x = [] ; xErr = []; y = []; yErr = [];


for i in range(len(ar)):
    x.append(ar[i][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])


xminorLocator = MultipleLocator(1)
yminorLocator = MultipleLocator(1)

xmajorLocator = MultipleLocator(5)
ymajorLocator = MultipleLocator(5)

ax = plt.subplot()


plt.plot(x, y, 'g^')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')

ex_slope = np.linspace(17, 40, 500)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[5:], y[5:])
print("slope = ", slope, "intercept = ", intercept, '\n')
plt.plot(ex_slope, ex_slope*slope+intercept,'g-.')


ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(14, 41)
plt.ylim(0, 31)

plt.title(u"Магнитная восприимчивость Gd "+r"$\chi(T)$")
plt.xlabel(u'$T, ^0C$')
plt.ylabel(r'$\frac{1}{\chi(T)}$')

plt.show()
