import matplotlib.pyplot as plt
import numpy as np


plt.style.use('_mpl-gallery')

file =  open("Files/draw_benchmarking.txt", "r")

lines = file.readlines()
file.close()

x = np.linspace(0, 100, len(lines))
y = np.array([ float(line) for line in lines])

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(
    xlim = (0, 100), xticks=np.arange(0, 100, 10),
    ylim = (0, 20000), yticks=np.arange(0, 20000, 1000),
)

plt.show()
