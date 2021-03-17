#Zadanie 10
#Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: 
#klucz to nazwa produktu a wartość to ilość. Funkcja ma zliczyć ile jest wszystkich 
#produktów w ogóle i zwracać tę wartość.

def produkty(**lista):
    suma=0
    for i in lista:
        suma+=int(lista[i])
    return suma

print(produkty(jablka="1",pomarancze="2",cytryny="3"))