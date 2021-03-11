#Napisz skrypt, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży 
#ale nie więcej jak 10.
#A
#AA
#AAA
#AAAA
#AAAAA
#AAAAAA
from sys import *
h=int(input("Podaj wysokosc nie większą niz 10: "))
if h<=10:
    for i in range(h):
        for j in range(i+1):
            stdout.write("A")
        stdout.write("\n")
else:
    print("Wysokośc wiezy nie moze byc wieksza niz 10")
