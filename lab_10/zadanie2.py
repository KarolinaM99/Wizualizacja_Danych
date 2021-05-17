import matplotlib.pyplot as plt
import numpy as np

x=range(1,21)
y=[1/y for y in x]
plt.plot(x,y,'g:>',label='f(x)=1/x')
plt.axis([0,len(x),0,1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.legend()
plt.show()