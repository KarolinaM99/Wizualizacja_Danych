#Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
#nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
#konstruktor – który nadaje wartości
#wyświetl_produkt() – drukuje informacje o produkcie na ekranie
#ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
#ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

class NaZakupy:
    nazwa_produktu=""
    ilosc=0
    jednostka_miary=""
    cena_jed=0

    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    
    def wyswietl_produkt(self):
        print("Nazwa produktu: ",self.nazwa_produktu)
        print("Ilosc: ",self.ilosc)
        print("Jednostka miary: ",self.jednostka_miary)
        print("Cena jednostkowa: ",self.cena_jed)
    
    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)
    
    def ile_kosztuje(self):
        print(self.ilosc*self.cena_jed)
    
zakupy=NaZakupy("Cukier",5,"kg",2.50)
zakupy.wyswietl_produkt()
zakupy.ile_produktu()
zakupy.ile_kosztuje()