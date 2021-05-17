import pandas as pd


def a(df):
    return df.Sprzedawca.unique()

def b(df):
    x=df.sort_values('Utarg',ascending=False)
    return x.head(5)

def c(df):
    return df.groupby(['Kraj']).agg({"idZamowienia":['count']})


df = pd.read_csv("lab_08/zamowienia.csv",header=0,delimiter=";")
print(a(df))
print(b(df))
