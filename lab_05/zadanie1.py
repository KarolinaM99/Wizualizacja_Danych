class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.szerokosc=szerokosc
        self.dlugosc=dlugosc

    def wyswietl_nazwe(self):
        return self.rodzaj

class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo

    def wyswietl_dane(self):
        return self.rozmiar,self.kolor,self.dla_kogo

class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra
        
    def wyswietl_dane(self):
        return self.rodzaj_swetra

material=Material("bawelna",5,5)
print(material.wyswietl_nazwe())
ubranie=Ubrania("S","Czarny","Damski")
print(ubranie.wyswietl_dane())
sweter=Sweter("golf")
print(sweter.wyswietl_dane())