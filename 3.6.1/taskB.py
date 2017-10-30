import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import interp1d
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
ar = open_file("input_taskB.txt")

x = []; xErr = []; y = []; yErr = []

for i in range(len(ar)):
    x.append(ar[i ][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])


xminorLocator = MultipleLocator(0.02)
yminorLocator = MultipleLocator(0.02)

xmajorLocator = MultipleLocator(0.1)
ymajorLocator = MultipleLocator(0.1)

ax = plt.subplot()

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

#ax.text(1.25, 0.85, r'$\nu_0$'+u' - резонансная частота'+'\n'+r'$U_0$'+u' - напряжение при'+'\n''резонансной частоте '+r'$\nu_0$', size='small', style='italic',
#        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})


slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope = ", slope, "intercept = ", intercept, '\n')

x_linreg = np.linspace(0, 1, 500)
y_linreg = x_linreg*slope+intercept
plt.plot(x_linreg, y_linreg, 'k', label = u"Экспериментальные данные")

th_slope = np.linspace(0, 1, 500)

plt.plot(th_slope, th_slope*0.5, 'k', ls='-.', label = u"Теоретические данные")

plt.plot(x, y, '.', color='k')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')



plt.xlim(0, 1.1)
plt.ylim(0, 0.55)
plt.title(u"В. Зависимость спектра от модуляуции")
plt.ylabel(r'$\frac{а_{бок}}{a_{осн}}$', size='x-large')
plt.xlabel(r'$m$', size='x-large')
plt.legend()

plt.show()