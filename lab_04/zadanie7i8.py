#Zad. 7 Stwórz klasę Robot, która będzie sterować ruchami robota. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla robota), i powinna mieć następujące metody:
#konstruktor – który nadaje wartość dla x, y i krok
#idz_w_gore(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#idz_w_dol(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#idz_w_lewo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#idz_w_prawo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
#pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne robota
#Stwórz instancję klasy i sprawdź jak działają wszystkie metody

class Robot:
    x=0
    y=0
    krok=1

    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    
    def idz_w_gore(self,ile):
        self.y+=ile*self.krok
    
    def idz_w_dol(self,ile):
        self.y-=ile*self.krok

    def idz_w_prawo(self,ile):
        self.x+=ile*self.krok
    
    def idz_w_lewo(self,ile):
        self.x-=ile*self.krok
    
    def pokaz_gdzie_jestes(self):
        print("X: ",self.x,", Y: ",self.y)

#Zad. 8
#Do klasy z wybranego poprzedniego zadania dołącz funkcję niszczenia obiektu.

    def __del__(self):
        del self.x
        del self.y
        del self.krok
        print("Robot zostal zniszczony")

robot=Robot(0,0,1)
robot.pokaz_gdzie_jestes()
robot.idz_w_dol(5)
robot.pokaz_gdzie_jestes()
robot.idz_w_gore(3)
robot.pokaz_gdzie_jestes()
robot.idz_w_lewo(3)
robot.pokaz_gdzie_jestes()
robot.idz_w_prawo(7)
robot.pokaz_gdzie_jestes()
