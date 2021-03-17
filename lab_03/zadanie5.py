#Zadanie 5
#Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe: Proste dane równaniami:
#y=a1x+b1, y=a2x+b2, są równolegle gdy a1=a2 prostopadłe gdy a1a2=-1

def prostorowno(a1,b1,a2,b2):
    if a1==a2:
        return "Proste sa rownolegle"
    elif a1*a2==-1:
        return "Proste sa prostopadle"
    else:
        return "Proste nie sa ani rownolegle, ani prostopadle"
    
print(prostorowno(3,4,3,2))
print(prostorowno(2,3,-1/2,5))
print(prostorowno(2,3,4,5))