import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

np.random.seed( 1968081 )

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n)+vmin

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
n=100

for c, m, zlow, zhigh in [('green', 'o', -50, -25), ( 'pink', '^', -30, -5), ('yellow','*',-10,-20),('darkblue','P',-20,-30),('cyan','p',-40,-10)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()