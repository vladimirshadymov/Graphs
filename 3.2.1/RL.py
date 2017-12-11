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

ar = open_file("RL_input.txt")

x = [];
xErr = [];
y = [];
yErr = [];

for i in range(len(ar)):
    x.append(ar[i][0]/np.pi)
    xErr.append(ar[i][1])
    y.append(ar[i][2]/np.pi)
    yErr.append(ar[i][3])

xminorLocator = MultipleLocator(0.125/2)
yminorLocator = MultipleLocator(0.125/2)

xmajorLocator = MultipleLocator(0.25)
ymajorLocator = MultipleLocator(0.25)

ax = plt.subplot()

plt.plot(x, y, 'g^')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
#plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')

ex_slope = np.linspace(0, 0.5, 500)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope = ", slope, "intercept = ", intercept, '\n')
plt.plot(ex_slope, ex_slope * slope + intercept, 'g-', label=u"Экспериментальные данные")

plt.plot(ex_slope, -ex_slope, "b-.", label=u"Теоретическая зависимость")

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(0, 0.51)
plt.ylim(-0.51, 0)

plt.title(u"Зависимость "+r"$\mathit{\psi}(\frac{\Omega L}{R_\Sigma})$")
plt.xlabel(r"$\arctan(\frac{\Omega L}{R_\Sigma})$, $\pi$")
plt.ylabel(r"$\psi$, $\pi$")
plt.legend(loc="best")

plt.show()
