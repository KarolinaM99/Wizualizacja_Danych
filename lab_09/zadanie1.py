import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile("lab_08/imiona.xlsx")
df = pd.read_excel(xlsx,"Arkusz1")
grupa=df.groupby(['Rok']).agg({'Liczba':['sum']})
print(grupa)
grupa.plot(xticks=grupa.index.values)
plt.legend()
plt.show()