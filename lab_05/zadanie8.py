class Wspak:
    samogloski={"a","e","y","i","o","u"}
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        if isinstance(data,str):
            self.data = data
        else:
            self.data=str(data)
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index >= len(self.data):
            raise StopIteration
        if self.data[self.index] in Wspak.samogloski:
            return self.data[self.index]

samogloski=Wspak("iidfres")
x=iter(samogloski)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))