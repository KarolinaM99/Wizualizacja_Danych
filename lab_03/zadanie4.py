#Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
#y = a x + b

def monotonicznosc(a,b):
    if a>0:
        return "Funkcja rosnaca"
    elif a<0:
        return "Funkcja malejaca"
    else:
        return "Funkcja stała"

print(monotonicznosc(2,0))
print(monotonicznosc(-2,0))
print(monotonicznosc(0,0))