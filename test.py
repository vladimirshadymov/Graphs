import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter



t = np.arange(0.0, 100.0, 0.1)

plt.plot(np.cos(t), np.sin(2*t))
plt.grid()

plt.show()
