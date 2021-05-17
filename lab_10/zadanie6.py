#Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8. 
#Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). 
#Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
#1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
#2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, 
#druga dla mężczyzn dla każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
#3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

import xlrd
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

xlsx=pd.ExcelFile('lab_08/imiona.xlsx')
df=pd.read_excel(xlsx)
wyk1=df.groupby(['Plec']).agg({'Liczba':['sum']})
wyk2k=df[df['Plec']=='K'].groupby(['Rok']).agg({'Liczba':['sum']})
wyk2m=df[df['Plec']=='M'].groupby(['Rok']).agg({'Liczba':['sum']})
wyk3=df.groupby(['Rok']).agg({'Liczba':['sum']})

plt.subplot(1,3,1)
plt.bar(['K','M'],[wyk1.values[0][0],wyk1.values[1][0]],color=['pink','green'])
plt.ylabel('Ilość narodzin')
plt.xlabel('Płeć')

plt.subplot(1,3,2)
plt.plot(df.Rok.unique(),[wyk2m.values[y][0] for y in range(len(wyk2m.values))],'pink',label="M")
plt.plot(df.Rok.unique(),[wyk2k.values[y][0] for y in range(len(wyk2k.values))],'green',label="K")
plt.ylabel('Ilosc urodzeń')
plt.xlabel('Rok')
plt.legend()

plt.subplot(1,3,3)
plt.bar(df.Rok.unique(),[wyk3.values[y][0] for y in range(len(wyk3.values))],color='green')
plt.ylabel('Ilosc urodzeń')
plt.xlabel('Rok')
plt.show()