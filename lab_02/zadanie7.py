#Zadanie 7
#Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie.
x=int(input("Podaj liczbę: "))
for i in range(1,10,1):
    print(x*x)
    x=int(input("Podaj liczbę: "))
