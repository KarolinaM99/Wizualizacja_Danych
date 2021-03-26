#Zad. 1
#Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
plik=open("lab_04_zadanie1.txt","w+")
for x in range (1,101): 
    if x%4==0:
        plik.write(str(x)+" ") 
plik.close()