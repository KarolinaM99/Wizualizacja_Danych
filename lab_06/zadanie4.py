import numpy as np
def funkcja(liczba,x):
    return np.logspace(1,x,num=x,base=liczba,dtype=int)
print(funkcja(2,5))