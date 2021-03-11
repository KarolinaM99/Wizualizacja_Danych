#Zadanie 2
#Zapisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez 
#siebie. Wynik wyświetla na ekranie (użyj instrukcji readline() i write()).
from sys import *
print("Podak pierwszą liczbę: ")
liczba1=stdin.readline()
print("Podaj drugą liczbę: ")
liczba2=stdin.readline()
print("Wynik mnozenia tych liczb to: ")
stdout.write(str(int(liczba1)*int(liczba2)))