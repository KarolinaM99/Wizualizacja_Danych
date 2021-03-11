#Zadanie 4
#Napisz skrypt, który pobiera od użytkownika liczbę i wypisuje na ekran wartość 
#bezwzględną tej liczby
liczba=int(input("Podaj liczbe: "))
if liczba>=0:
    print(liczba)
else:
    print(-1*liczba)