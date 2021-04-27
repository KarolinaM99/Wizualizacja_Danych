import numpy as np
a=np.arange(12)
print(a)
b=a.reshape(3,4)
for i in b.flat:
    print(i)
c=a.reshape(4,3)
for i in c.flat:
    print(i)
d=a.reshape(2,6)
for i in d.flat:
    print(i)