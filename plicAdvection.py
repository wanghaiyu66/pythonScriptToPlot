#import matplotlib.pyplot as plt
#x = range(1,10)
#y = range(1,10)
#plt.plot(x,y,'o')
#plt.show()

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# meta-intersection
E   = [1, 0.3]
F   = [0, 0.8]
EFx = [E[0], F[0]]
EFy = [E[1], F[1]]

G   = 0.5*(np.array(E)+np.array(F))
EF  = np.array(F) - np.array(E)
n   = -0.1*np.array([EF[1], -EF[0]])/np.linalg.norm(EF)

pt0 = [0, 0]
pt1 = [1, 0]
pt2 = [1, 1]
pt3 = [0, 1]
ptx = [pt0[0], pt1[0], pt2[0], pt3[0], pt0[0]]
pty = [pt0[1], pt1[1], pt2[1], pt3[1], pt0[1]]

P   = [0.9, 0]
Q   = [0.9, 1]
S   = [0.9, 0.35]
PQx = [P[0], Q[0]]
PQy = [P[1], Q[1]]

liquidx = [pt0[0], pt1[0], E[0], F[0]]
liquidy = [pt0[1], pt1[1], E[1], F[1]]

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 18,
        }

plt.figure(figsize=(10,10))
plt.axis('equal')
plt.axis('off')
plt.plot(ptx, pty, marker = 'o', color = 'k')
plt.fill(liquidx, liquidy, zorder=0, alpha=0.5)
plt.plot(EFx, EFy, marker = 'o', color = 'b')
plt.plot(PQx, PQy, marker = 'o', color = 'r')
plt.plot(S[0], S[1], marker = 'o', color = 'r')
# n
plt.arrow(G[0], G[1], n[0], n[1], head_width=0.03, head_length=0.08, fc='b', ec='b')
# advection velocity
plt.plot(1.21, 0.5, marker = 'o', color = 'w')
plt.arrow(1.0, 0.5, 0.1, 0, head_width=0.03, head_length=0.08, fc='k', ec='k')
# delta x
lsx = [0.9, 1.0]
lsy = [0.1, 0.1]
plt.arrow(0.85, 0.1, 0.03, 0, head_width=0.01, head_length=0.02, fc='k', ec='k')
plt.arrow(1.2, 0.1, -0.18, 0, head_width=0.01, head_length=0.02, fc='k', ec='k')
plt.plot(lsx, lsy, color = 'k')
# text
delta = -0.04
plt.text(pt0[0]+delta, pt0[1]+delta, 'A', fontdict=font)
plt.text(pt1[0]+delta, pt1[1]+delta, 'B', fontdict=font)
plt.text(pt2[0]+delta, pt2[1]+delta, 'C', fontdict=font)
plt.text(pt3[0]+delta, pt3[1]+delta, 'D', fontdict=font)
plt.text(E[0]+delta, E[1]+delta, 'E', fontdict=font)
plt.text(F[0]+delta, F[1]+delta, 'F', fontdict=font)
plt.text(P[0]+delta, P[1]+delta, 'P', fontdict=font)
plt.text(Q[0]+delta, Q[1]+delta, 'Q', fontdict=font)
plt.text(S[0]+delta, S[1]+delta, 'S', fontdict=font)
plt.text(G[0]+0.01, G[1]+0.01, r'$ \overrightarrow{n} = \nabla \alpha$', fontdict=font)
plt.text(0.4, 0.15, r'$ \alpha = S_{ABEF} / S_{ABCD}$', fontdict=font)
plt.text(1.05, 0.505, r'$ \overrightarrow{u} $', fontdict=font)
#plt.text(1.05, 0.4, r'$ \alpha_{f} = S_{PBES} / S_{PBCQ} $', fontdict=font)
plt.text(1.05, 0.11, r'$|\overrightarrow{u}| \delta t$', fontdict=font)

plt.show()
