import numpy as np
def funkcja(n):
    return np.array(n*[np.arange(n)])
print(funkcja(3))