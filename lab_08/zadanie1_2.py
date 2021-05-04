import pandas as pd
import numpy as np
import xlrd
import openpyxl
def a(df):
    return (df[df['Liczba']>1000])

def b(df):
    return (df[df['Imie']=="KAROLINA"])

def c(df):
    return (df.agg({'Liczba':['sum']}))

def d(df):
    x=df[(df['Rok']>=2000)&(df['Rok']<=2005)]
    return (x.agg({'Liczba':['sum']}))

def e(df):
    return (df.groupby(['Plec']).agg({'Liczba':['sum']}))

def f(df):
   print("-----")

def g(df):
    dziewczynki=df[df['Plec']=='K']
    chlopcy=df[df['Plec']=='M']
    dz=dziewczynki.sort_values("Liczba",ascending=False)
    ch=chlopcy.sort_values("Liczba",ascending=False)
    return dz.head(1),ch.head(1)



xlsx = pd.ExcelFile("lab_08/imiona.xlsx")
df = pd.read_excel(xlsx,"Arkusz1")
print(a(df))
print(b(df))
print(c(df))
print(d(df))
print(e(df))
f(df)
print(g(df))