import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rc
import numpy as np
# % matplotlib inline

fontAxis = 24
fontTitle = 36
N = 5
x = np.linspace(-1, 1, 100)
colors = cm.hsv(np.linspace(0, 1, N + 1))

plt.close("all")

fig = plt.figure()
fig.patch.set_facecolor('white')

ax = plt.subplot(111)
for i in range(0, N):
    y = pow(x, i + 1)
    plt.plot(x, y, color=colors[i], linestyle='-', linewidth=2)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
rc('font', size=fontAxis)

plt.xlabel('$x$', fontsize=fontAxis, fontweight='bold')
plt.ylabel('$y$', fontsize=fontAxis, fontweight='bold')
plt.title('$ y = x^n $', fontsize=fontTitle, fontweight='bold')
plt.grid(True)
plt.hold(True)
plt.show()