#Zadanie 6
#Napisz pętlę, która wyświetla liczby podzielne przez 5 z zakresu <0,50>
for x in range(0,51,1):
    if x!=0 and x%5==0:
        print(str(x)+" ")