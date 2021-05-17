#Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. 
#Dodaj etykietę do linii wykresu i wyświetl legendę. 
#Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).
import matplotlib.pyplot as plt

x=range(1,21)
y=[1/y for y in x]
plt.plot(x,y, label='f(x)=1/x')
plt.axis([0,len(x),0,1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()