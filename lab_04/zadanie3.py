#Zad. 3
#Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie 
#wyświetl je na ekranie.
with open("lab_04_zadanie3.txt","w") as plik:
    plik.write("Ola ma kota\n")
    plik.write("Ola ma psa\n")
with open("lab_04_zadanie3.txt","r") as plik:
    for linia in plik:
        print(linia, end="")