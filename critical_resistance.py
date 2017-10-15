import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

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
ar = open_file("input1.txt")

x = [] ; xErr = []; y = []; yErr = [];


for i in range(len(ar)):
    x.append(ar[i ][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])


yline = []
xline = np.arange(0, 4, 0.01)
for x1 in xline:
    yline.append(8.46)

xminorLocator = MultipleLocator(0.1)
yminorLocator = MultipleLocator(1)

xmajorLocator = MultipleLocator(1)
ymajorLocator = MultipleLocator(5)

fig, ax = plt.subplots()


plt.plot(x, y, '.', color='k')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')

a = np.arange(min(x)-1, max(x)+1, 0.001)
p = np.poly1d(np.polyfit(x, y, 1))
plt.plot(a, p(a), color='k')
plt.plot(xline, yline, 'c-.')
print('Уравнение', np.poly1d(np.polyfit(x, y, 1)))
print('a=', np.polyfit(x, y, 1, cov = True)[0][0], 'b=', np.polyfit(x, y, 1, cov = True)[0][1])
print(np.polyfit(x, y, 1, cov = True))

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(0, 3.5)
plt.ylim(6, 21)

plt.title(u'Зависимость максимального отклонения от сопротивления')
plt.ylabel(r'$\mathit{x}, см$', fontsize=10)
plt.xlabel(r'$\frac{1}{\mathit{R_0+R}}, 10^{-4} \frac{1}{Ом}$', fontsize=13)

plt.show()
