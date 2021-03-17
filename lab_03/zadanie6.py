#Zadanie 6
#Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość promienia. Funkcja ma przyjmować argumenty domyślne: Równanie okręgu dane jest wzorem:
#(x-a)2+(y-b)2=r2 gdzie (a,b) to środek okręgu a r to promień okręgu.

from math import sqrt
def promien(x,y,a,b):
    return sqrt((x-a)**2+(y-b)**2)
print(promien(1,2,3,4))