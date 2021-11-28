import matplotlib.pyplot as plt
import numpy as np
import math


plt.style.use('_mpl-gallery')


#make data
x = np.linspace(0, 10, 100)
y = (math.e ** x) ** (1 / 10)


#plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(
    xlim=(-10, 10), xticks=np.arange(-10, 10),
    ylim=(0, 10), yticks=np.arange(1, 8),
)

plt.show()



