import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

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

ar = open_file("decrease100om.txt")

x = [] ; xErr = []; y = []; yErr = [];


for i in range(len(ar)):
    x.append(ar[i ][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])



xminorLocator = MultipleLocator(0.2)
yminorLocator = MultipleLocator(0.1)

xmajorLocator = MultipleLocator(1)
ymajorLocator = MultipleLocator(0.2)

fig, ax = plt.subplots()


plt.plot(x, y, '.', color='k')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')

a = np.arange(min(x)-1, max(x)+1, 0.001)
p = np.poly1d(np.polyfit(x, y, 1))
plt.plot(a, p(a), color='k')
print('Уравнение', np.poly1d(np.polyfit(x, y, 1)))
print('a=', np.polyfit(x, y, 1, cov = True)[0][0], 'b=', np.polyfit(x, y, 1, cov = True)[0][1])
print(np.polyfit(x, y, 1, cov = True))

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(0, 3.1)
plt.ylim(0, 1.2)

plt.title(u'Затухание колебаний R=100 Ом')
plt.xlabel(u'$n$')
plt.ylabel(r'$ln\frac{U_k}{U_{k+n}}$')

plt.show()