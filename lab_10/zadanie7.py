import xlrd
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

xlsx=pd.ExcelFile('lab_08/imiona.xlsx')
df=pd.read_excel(xlsx)

wyk2k=df[df['Plec']=='K'].groupby(['Rok']).agg({'Liczba':['sum']})
wyk2m=df[df['Plec']=='M'].groupby(['Rok']).agg({'Liczba':['sum']})

plt.bar(df.Rok.unique(),[wyk2m.values[y][0] for y in range(len(wyk2m.values))],color='red',label="M")
plt.bar(df.Rok.unique(),[wyk2k.values[y][0] for y in range(len(wyk2k.values))],color='blue',label="K",bottom=[wyk2m.values[y][0] for y in range(len(wyk2m.values))])
plt.ylabel('Ilosc urodzeń')
plt.xlabel('Rok')
plt.legend()
plt.show()