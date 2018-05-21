import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


horix = [0, 0.8]
horiy = [0, 0]
liquidx = [0.2, 0.6, 0.6, 0.2]
liquidy = [0, 0, -0.1, -0.1]

font = {'family': 'mono',
        'color':  'black',
        'weight': 'normal',
        'style':  'italic',
        'size': 20,}

plt.axis('equal')
plt.axis('off')
plt.plot(horix, horiy, 'k')
plt.text(0, 0.03, 'vapor', fontdict=font)
plt.text(0, -0.07, 'liquid', fontdict=font)
plt.text(0.6, 0.03, r'$T_{interface} = T_{sat}$', fontdict=font)
plt.text(0.4, 0.2, r'$\dot{M}, (kg/s)$', fontdict=font)
t = np.arange(0.0, 0.1, 0.0001)
s = -0.02*np.sin(40.01 * np.pi * t)
plt.plot(0.5+s, t, color='dodgerblue')
plt.arrow(0.5, 0.1, 0, 0.05, head_width=0.01, head_length=0.04, fc='dodgerblue', ec='dodgerblue')
plt.plot(0.4+s, t, color='dodgerblue')
plt.arrow(0.4, 0.1, 0, 0.05, head_width=0.01, head_length=0.04, fc='dodgerblue', ec='dodgerblue')
plt.plot(0.3+s, t, color='dodgerblue')
plt.arrow(0.3, 0.1, 0, 0.05, head_width=0.01, head_length=0.04, fc='dodgerblue', ec='dodgerblue')
plt.fill(liquidx, liquidy, zorder=0, color='dodgerblue', alpha=0.5)

#plt.arrow(0.4, 0.0, 0, -0.05, head_width=0.01, head_length=0.04, fc='k', ec='k')
#plt.text(0.41, -0.1, r'$\overrightarrow{A}$', fontdict=font)
plt.show()
