#Zadanie 9
#Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów ciągu.

def iloczyn(* liczba):
    if len(liczba)!=0:
        iloczyn=1
        for i in liczba:
            iloczyn*=i
        return iloczyn
    else:
        return 0

print(iloczyn(1,2,3,2,2))