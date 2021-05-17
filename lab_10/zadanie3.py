#Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. 
#Dodaj etykiety i legendę do wykresu.
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,30,0.1)
sinus=np.sin(x)
cosinus=np.cos(x)
plt.plot(x,sinus,label='sin(x)')
plt.plot(x,cosinus,label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()