import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
# % matplotlib
# inline
# ===================

colortable = ['r', 'b', 'c', 'k', 'g', 'm', 'r', 'b',
              'c', 'k', 'g', 'm', 'r', 'b', 'c', 'k', 'g', 'm',
              'r', 'b', 'c', 'k', 'g', 'm', 'r', 'b',
              'c', 'k', 'g', 'm', 'r', 'b', 'c', 'k', 'g', 'm']
markertable = ['o', 's', 'v', '^', 'o', 's', 'v',
               '^', 'o', 's', 'v', '^', 'o', 's', 'v', '^'
                                                       'o', 's', 'v', '^', 'o', 's', 'v',
               '^', 'o', 's', 'v', '^', 'o', 's', 'v', '^']

# move to the target folder
path = '/Users/yiyi/Desktop/Final_v3/STT5438_'
os.chdir(path)

# get filenames in the folder
fileformat = '_8000MHz.dat'
fontAxis = 20
fontLabel = 14
fontTitle = 28

fig = plt.figure(figsize = (12, 10), facecolor='white')

i = 0 # starting from Index = 0
for file in os.listdir('.'):
    if file.endswith(fileformat):
        f = file
        # Load data files into x, y

        rawdata = []
        for line in open(f, 'r').readlines():
            rawdata.append(line.split())

        del rawdata[len(rawdata) - 1]  # remove last data point

        # 1 --> H, 6 --> S12_real, 7 --> S12_imag
        indexH = 1
        indexS12_real = 6

        H = []
        S12_real = []

        for element in rawdata[:]:
            H.append(element[indexH])
            S12_real.append(element[indexS12_real])
        x = H
        y = S12_real

        # Plot out x-y
        xlabelname = r'$H_{//}(T)$'
        ylabelname = r'$S_{12}^{real}$'
        titlename = r'$S_{12}^{real}-H_{//}$'

        ax = fig.add_subplot(111)
        rc('font', size=fontLabel)

        plt.hold(True)
        lines = plt.plot(x, y, linestyle='-')

        plt.setp(lines, color=colortable[i], linewidth=2.0)
        plt.xlabel(xlabelname, fontsize=fontAxis, fontweight='bold')
        plt.ylabel(ylabelname, fontsize=fontAxis, fontweight='bold')
        plt.title(titlename, fontsize=fontTitle, fontweight='bold')
        plt.grid(False)
        plt.hold(True)
        plt.show()

        xmin = round(float(min(x)), 2)
        xmax = round(float(max(x)), 2)
        ymin = round(float(min(y)), 4)
        ymax = round(float(max(y)), 4)

        ax.set_xlim(xmin - (xmax - xmin) * 0.1, xmax + (xmax - xmin) * 0.1)
        ax.set_ylim(ymin - (ymax - ymin) * 0.1, ymax + (ymax - ymin) * 0.1)
        # ax.annotate(r'$x-y$', xy=(xmax*0.1, ymax-(ymax-ymin)*0.1))
        i = i + 1

plt.show()
