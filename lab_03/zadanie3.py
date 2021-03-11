#Zadanie 3
#Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie 
#nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). 
#Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą 
#produkty, których wartość to sztuki.
produkty={"woda":"litry","pomarancze":"sztuki","cukier":"kg"}
print(produkty)
produkty2={key for key in produkty if produkty[key]=="sztuki"}
print(produkty2)