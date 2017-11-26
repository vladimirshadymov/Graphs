import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter



t = np.arange(0.0, 10.0, 0.1)

a = 1.9
plt.plot(t, 1/((1-t**2/a)**2+t**2)**0.5)
plt.grid()

plt.show()
