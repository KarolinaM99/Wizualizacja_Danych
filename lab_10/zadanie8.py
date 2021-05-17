#Napisz funkcję, która losowo rzuca dwiema kostkami k6 n razy. 
#Wynik rzutów zapisywany jest w postaci listy sum oczek z tych dwóch kostek. 
#Np. rzucaj(6) generuje 6 rzutów kostkami i zwraca wektor 6 sum oczek każdego rzutu. 
#Po zakończeniu funkcji wyświetlaj histogram sumy rzutów. Dodaj stosowne etykiety do wykresu.
import numpy as np
import matplotlib.pyplot as plt 

def rzucaj(n):
    return[(np.random.randint(1,6))+(np.random.randint(1,6)) for x in range(n)]

rzuty=rzucaj(10)
print(rzuty)
plt.hist(rzuty,bins=30,facecolor='green',alpha=0.75)
plt.xlabel('Wartości')
plt.ylabel('Ilosc rzutow')
plt.title('Histogram')
plt.grid(True)
plt.show()