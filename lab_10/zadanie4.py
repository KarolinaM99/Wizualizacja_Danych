import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,30,0.1)
sinus1=2+np.sin(x)
sinus2=np.sin(-x)
plt.plot(x,sinus1,label='sin(x)')
plt.plot(x,sinus2,label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres sin(x), sin(x)')
plt.legend(loc=6)
plt.show()