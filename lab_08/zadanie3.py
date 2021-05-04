import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime 
def a(df):
    return df.Sprzedawca.unique()

def b(df):
    x=df.sort_values('Utarg',ascending=False)
    return x.head(5)

def c(df):
    return df.groupby(['Kraj']).agg({"idZamowienia":['count']})


df = pd.read_csv("lab_08/zamowienia.csv",delimiter=";")
print(a(df))
print(b(df))
print(c(df))