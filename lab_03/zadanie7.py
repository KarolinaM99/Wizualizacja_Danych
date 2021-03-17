#Zadanie 7
#Zdefiniuj funkcję, która oblicza długość przeciwprostokątnej, wykorzystując twierdzenie pitagorasa. Proszę podać wartości domyślne dla funkcji

from math import *
def przeciwprostokatna(a,b):
    if b!=0:
        return sqrt(pow(a,2)+pow(b,2))
    return a*sqrt(2)
print(przeciwprostokatna(2,0))
print(przeciwprostokatna(3,2))