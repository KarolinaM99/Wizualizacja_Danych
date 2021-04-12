import numpy as np
def funkcja(dlugosc):
    return np.diag([x for x in range(dlugosc,0,-1) ])
print(funkcja(5))