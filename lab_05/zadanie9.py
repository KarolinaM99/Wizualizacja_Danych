def parzyste(data):
    for index in range(0,len(data)-1,2):
        yield data[index]

imie=parzyste("Karolina")
print(next(imie))
print(next(imie))
print(next(imie))
print(next(imie))
