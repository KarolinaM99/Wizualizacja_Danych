#Zadanie 2
#Wygeneruj losowo macierz 4x4 i wykorzystując Python Comprehension zdefiniuj 
#listę, która będzie zawierała tylko elementy znajdujące się na przekątnej.
from random import *
macierz=[[round(random()*1000) for y in range(1+4*x,5+4*x)] for x in range(4)  ]
print(macierz)
przekatna = [macierz[x][x] for x in range(4)]
print(przekatna)