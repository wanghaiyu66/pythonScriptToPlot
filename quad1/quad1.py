#import matplotlib.pyplot as plt
#x = range(1,10)
#y = range(1,10)
#plt.plot(x,y,'o')
#plt.show()

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches



# neighbour-intersection
#E   = [0.9, 0]
#F   = [0, 0.6]

# meta-intersection
E   = [1, 0.3]
F   = [0, 0.8]

G   = 0.5*(np.array(E)+np.array(F))
EF  = np.array(F) - np.array(E)
n   = 0.1*np.array([EF[1], -EF[0]])/np.linalg.norm(EF)

pt0 = [0, 0]
pt1 = [1, 0]
pt2 = [1, 1]
pt3 = [0, 1]
ptx = [pt0[0], pt1[0], pt2[0], pt3[0], pt0[0]]
pty = [pt0[1], pt1[1], pt2[1], pt3[1], pt0[1]]

EFx = [E[0], F[0]]
EFy = [E[1], F[1]]

liquidx = [E[0], pt2[0], pt3[0], F[0]]
liquidy = [E[1], pt2[1], pt3[1], F[1]]

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 18,
        }

plt.figure(figsize=(10,10))
plt.axis('off')
plt.plot(ptx, pty, marker = 'o', color = 'k')
plt.fill(liquidx, liquidy, zorder=0, alpha=0.5)
plt.plot(EFx, EFy, marker = 'o', color = 'b')

plt.arrow(G[0], G[1], n[0], n[1], head_width=0.05, head_length=0.1, fc='b', ec='b')
# text
delta = -0.04
plt.text(pt0[0]+delta, pt0[1]+delta, 'A', fontdict=font)
plt.text(pt1[0]+delta, pt1[1]+delta, 'B', fontdict=font)
plt.text(pt2[0]+delta, pt2[1]+delta, 'C', fontdict=font)
plt.text(pt3[0]+delta, pt3[1]+delta, 'D', fontdict=font)
plt.text(E[0]+delta, E[1]+delta, 'E', fontdict=font)
plt.text(F[0]+delta, F[1]+delta, 'F', fontdict=font)

plt.show()
