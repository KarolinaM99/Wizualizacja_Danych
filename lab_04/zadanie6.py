#Zad. 6
#Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
#sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
#sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
#sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
#wyświetl_wyrazy – wyświetla podane wyrazy
#Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Slowa:
    slowo1=""
    slowo2=""

    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    
    def sprawdz_czy_palindrom(self):
        print(self.slowo1)
        if self.slowo1!=self.slowo1[::-1]:
            print("Nie jest palindromem")
        else:
            print("Jest palindromem")
        print(self.slowo2)
        if self.slowo2!=self.slowo2[::-1]:
            print("Nie jest palindromem")
        else:
            print("Jest palindromem")
    
    def sprawdz_czy_metagramy(self):
        x=False
        if len(self.slowo1)==len(self.slowo2):
            z=0
            for i in range(len(self.slowo1)):
                if self.slowo1[i]!=self.slowo2[i]:
                    z+=1
            if z==1:
                x=True
        if x:
            print("Słowa są meragramami")
        else:
            print("Słowa nie są metagramami")
        
    def sprawdz_czy_anagramy(self):
        x=True
        if len(self.slowo1)==len(self.slowo2):
            z=self.slowo2
            for znak in self.slowo1:
                if znak in z:
                    i=z.index(znak)
                    z=z[:i]+z[i+1:]
                else:
                    x=False
        else:
            x=False
        if x:
            print("Słowa są anagramami")
        else:
            print("Słowa nie są anagramami")
        
    
    def wyswietl_wyrazy(self):
        print(self.slowo1,", ",self.slowo2,"\n")
        
slowa=Slowa("kajak","mata")
slowa.wyswietl_wyrazy()
slowa.sprawdz_czy_palindrom()
slowa2=Slowa("mata","tata")
slowa2.wyswietl_wyrazy()
slowa2.sprawdz_czy_metagramy()
slowa3=Slowa("tama","mata")
slowa3.wyswietl_wyrazy()
slowa3.sprawdz_czy_anagramy()