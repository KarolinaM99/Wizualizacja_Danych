def ciag():
    x=0
    y=1
    for i in range(100):
        z=x+y
        yield z
        x=y
        y=z
    
ciag=ciag()
for i in range(100):
    print(next(ciag))