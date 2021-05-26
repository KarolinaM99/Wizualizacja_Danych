import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()

ax = fig.add_subplot( 121 , projection = '3d' )
n = 20
xs = randrange(n, 0, 100)
ys = randrange(n, 0, 100)
zs = randrange(n, 0, 100)
ax.scatter(xs, ys, zs, c='green')
ax.set_xlabel( 'X Label')
ax.set_ylabel( 'Y Label')
ax.set_zlabel( 'Z Label')

ax=fig.add_subplot( 122 , projection = '3d' )
n=5
xs = randrange(n, 0, 100)
ys = randrange(n, 0, 100)
zs = randrange(n, 0, 100)
ax.scatter(xs, ys, zs, c='darkblue')
ax.set_xlabel( 'X Label')
ax.set_ylabel( 'Y Label')
ax.set_zlabel( 'Z Label')

plt.show()