#Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
#wyświetl_dane – drukuje elementy na ekran
#pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
#pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
#policz_sume – liczy sume elementow
#policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
#Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class ciagi_aryt():
    a=1
    r=0
    ilosc=0

    def wyswietl_dane(self):
        print("Pierwszy wyraz ciagu: ",self.a)
        print("Roznica: ",self.r)
        print("Ilosc: ",self.ilosc)
    
    def pobierz_elementy(self,a,r):
        self.a=a
        self.r=r
    
    def pobierz_parametry(self,a,r,ilosc):
        self.a=a
        self.r=r
        self.ilosc=ilosc
    
    def policz_sume(self):
        return ((self.a+(self.a+self.r*(self.ilosc-1)))/2)*self.ilosc
    
    def policz_elementy(self):
        lista=[self.a+self.r*1 for i in range (self.ilosc)]
        return lista

ciag=ciagi_aryt()
ciag.pobierz_parametry(1,3,2)
print("Elementy: ",ciag.policz_elementy())
print("Suma: ",ciag.policz_sume())
print(ciag.wyswietl_dane())
