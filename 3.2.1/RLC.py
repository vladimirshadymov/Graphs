import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy import interpolate


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

ar = open_file("RLC_input.txt")

x = [];
xErr = [];
y = [];
yErr = [];

for i in range(len(ar)):
    x.append(ar[i][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2]/np.pi)
    yErr.append(ar[i][3])

xminorLocator = MultipleLocator(0.1)
yminorLocator = MultipleLocator(0.125/2)

xmajorLocator = MultipleLocator(0.5)
ymajorLocator = MultipleLocator(0.25)

ax = plt.subplot()

plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
#plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')

ex_slope_0 = np.linspace(x[0], x[23], 500)
ex_slope_100 = np.linspace(x[24], x[-1], 500)

x1 = x[:24]
y1 = y[:24]
x2 = x[24:]
y2 = y[24:]

plt.plot(x[:24], y[:24], 'g^')
plt.plot(x[24:], y[24:], 'bs')

x1.pop(-4)
y1.pop(-4)
x1.pop(5)
y1.pop(5)
x1.pop(6)
y1.pop(6)
x1.pop(-5)
y1.pop(-5)

x2.pop(-3)
y2.pop(-3)
x2.pop(-5)
y2.pop(-5)
x2.pop(-10)
y2.pop(-10)

spline0 = interpolate.interp1d(x1, y1, kind=3)
spline100 = interpolate.interp1d(x2, y2, kind=3)

#print("slope = ", slope, "intercept = ", intercept, '\n')
plt.plot(ex_slope_0, spline0(ex_slope_0), 'g-', label=u"R = 0 Ом")
plt.plot(ex_slope_100, spline100(ex_slope_100), "b-", label=u"R = 100 Ом")

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.ylim(-0.51, 0.51)
plt.xlim(0.4, 1.82)

plt.title(u"Зависимость "+r"$\mathit{\psi}(\frac{\nu}{\nu_0})$")
plt.xlabel(r"$\frac{\nu}{\nu_0}$")
plt.ylabel(r"$\psi$, $\pi$")
plt.legend(loc="best")

plt.show()