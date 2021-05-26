import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


fig=plt.figure()
ax=fig.gca(projection = '3d')
t=np.linspace(0, 3*np.pi, 100)
z=t
x=np.sin(z)
y=2*np.cos(z)
ax.plot(x, y, z, label='zadanie1')
ax.legend()
plt.show()