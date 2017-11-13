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

ar = open_file("input_resistance.txt")

x = [] ; xErr = []; y = []; yErr = [];


for i in range(len(ar)):
    x.append(ar[i ][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])


xminorLocator = MultipleLocator(20)
yminorLocator = MultipleLocator(0.002)

xmajorLocator = MultipleLocator(100)
ymajorLocator = MultipleLocator(0.01)

ax = plt.subplot()


plt.plot(x, y, 'g^')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')


ex_slope = np.linspace(0, 1000, 500)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope = ", slope, "intercept = ", intercept, '\n')
plt.plot(ex_slope, ex_slope*slope+intercept, ls='-', label=u"Экспериментальная зависимость")


th_slope = np.linspace(0, 1000, 500)
slope0 = 0.05*10**(-3)*0.7069
plt.plot(th_slope, th_slope*slope0, 'k', ls='-.', label=u"Теоретическая зависимость")


ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(0, 1000)
plt.ylim(0, 0.05)

plt.title(u'')
plt.title(u"Период колебаний")
plt.xlabel(u'$R, кОм$')
plt.ylabel(u'$T, c$')
plt.legend()

plt.show()