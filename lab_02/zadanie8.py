#Zadanie 8
#Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście. 
#Wykorzystaj pętle while.
lista=[]
x=0
while x<10:
    liczba=int(input("Podaj liczbę: "))
    lista.append(liczba)
    x+=1
print(lista)