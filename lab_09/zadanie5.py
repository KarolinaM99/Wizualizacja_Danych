import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lab_08/zamowienia.csv",header=0,delimiter=";")
grupa=df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
print(grupa)
wykres=grupa.plot.bar()
wykres.legend()
plt.show()
