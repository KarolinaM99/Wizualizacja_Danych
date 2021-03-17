#Zadanie 8
#Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu arytmetycznego. 
#Funkcja niech przyjmuje jako parametry: a1 (wartość początkowa), 
#r (wielkość o ile rosną kolejne elementy) i ile_elementów (ile elementów ma sumować). 
#Ponadto funkcja niech przyjmuje wartości domyślne: a1= 1, r=1, ile=10.

def suma(a1=1,r=1,ile=10):
    if ile!=1:
        return a1+suma(a1+r,r,ile-1)
    return a1
print(suma(1,2,3))