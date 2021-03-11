#Zadanie 9
#Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry. 
#Wynik wyświetla na ekranie. Wykorzystaj pętle while.
liczba=int(input("Podaj liczbę wielocyfrową: "))
suma=0
while(liczba!=0):
    suma+=liczba%10
    liczba//=10
print(suma)