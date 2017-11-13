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

ar = open_file("input_vach.txt")

x = [] ; xErr = []; y = []; yErr = [];


for i in range(len(ar)):
    x.append(ar[i ][0])
    xErr.append(ar[i][1])
    y.append(ar[i][2])
    yErr.append(ar[i][3])


x_icrease = x[:11]
x_icrease_err = xErr[:11]
y_icrease = y[:11]
y_icrease_err = yErr[:11]
x_decrease = x[11:]
x_decrease_err = xErr[11:]
y_decrease = y[11:]
y_decrease_err = yErr[11:]


xminorLocator = MultipleLocator(1)
yminorLocator = MultipleLocator(0.2)

xmajorLocator = MultipleLocator(5)
ymajorLocator = MultipleLocator(1)

ax = plt.subplot()


plt.plot(x_icrease, y_icrease, 'r^')
plt.plot(x_decrease, y_decrease, 'gs')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.errorbar(x, y, xerr=xErr, yerr=yErr, ecolor='k', capsize=3, elinewidth=1, fmt=' ')



slope, intercept, r_value, p_value, std_err = stats.linregress(x_decrease[:11], y_decrease[:11])
print("slope = ", slope, "intercept = ", intercept, '\n')

th_slope = np.linspace(78, 114, 5)

plt.plot(th_slope, th_slope*slope+intercept, 'k', ls='-.', label=u"Убывание")

slope, intercept, r_value, p_value, std_err = stats.linregress(x_icrease, y_icrease)
print("slope = ", slope, "intercept = ", intercept, '\n')
th_slope = np.linspace(95, 114, 5)
plt.plot(th_slope, th_slope*slope+intercept, 'Blue', ls='-.', label=u"Возрастание")

line = np.linspace(0.22, 6.9, 500)
plt.plot([sum((line-intercept)/slope-5.1*line-0.5)/500]*500, line, "green", ls="-.", label=u"ВАХ стабилитрона")

i_st = []
for i in range(len(y_icrease)):
    i_st.append((y_icrease[i]-intercept)/slope-5.1*y_icrease[i])

plt.plot(i_st, y_icrease, "r^", label=u"ВАХ стабилитрона")

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.xlim(70, 120)
plt.ylim(0, 7)

plt.title(u'Вольт-амперная характеристика стабилитрона')
plt.xlabel(u'$U, В$')
plt.ylabel(u'$I, мА$')
plt.legend()

plt.show()