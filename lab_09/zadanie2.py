import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile("lab_08/imiona.xlsx")
df = pd.read_excel(xlsx,"Arkusz1")
grupa=df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres=grupa.plot.bar()
wykres.set_ylabel("Liczba dzieci (mln)")
wykres.set_xlabel("Plec")
wykres.legend()
plt.title("Liczba urodzonych dzieci")
plt.show()