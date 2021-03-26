#Zad. 2
#Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.
with open("lab_04_zadanie1.txt","r") as plik:
    for linia in plik:
        print(linia,end="")