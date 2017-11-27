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

ex_slope = np.linspace(17, 40, 500)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[5:], y[5:])
print("slope = ", slope, "intercept = ", intercept, '\n')
plt.plot(ex_slope, ex_slope*slope+intercept,'g-.', label=u"Данные лабораторной \n работы № 3.4.2 \n"+r'$\Theta_p = 18.5^oC$')

x_ISU_cgs = x_ISU_SI = np.linspace(18, 70, 20)
y_ISU_cgs = 0.019789*(x_ISU_cgs+273.15)-6.342
y_ISU_SI = y_ISU_cgs/(4*np.pi)*1000

plt.plot(x_ISU_SI, y_ISU_SI, 'r-', label='Данные ISU, \nаппроксимированный диапазон \nтемператур 350-875 '+'$^o$'+'K '+r'$\Theta_p = 47.3^oC$')


x_ISU_cgs = x_ISU_SI = np.linspace(18, 70, 20)
y_ISU_cgs = 0.01667*(x_ISU_cgs+273.15)-5.002217
y_ISU_SI = y_ISU_cgs/(4*np.pi)*1000

plt.plot(x_ISU_SI, y_ISU_SI, 'b--', label='Данные ISU, \nаппроксимированный диапазон \nтемператур 350-470 '+'$^o$'+'K '+r'$\Theta_p = 27.0^oC$')


ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(14, 70)
plt.ylim(0, 31)

plt.title(u"Магнитная восприимчивость Gd "+r"$\chi(T)$"+u"в СИ")
plt.xlabel(u'$T, ^0C$')
plt.ylabel(r'$\frac{1}{\chi(T)}$')
plt.legend(loc='best')

plt.show()
