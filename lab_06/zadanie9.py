import numpy as np

def fib(x):
    if x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)

fibo=np.array([fib(x) for x in range(9)])
fibo=fibo.reshape((3,3))
print(fibo)