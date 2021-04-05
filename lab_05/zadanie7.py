class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=2
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

imie=Wspak("Karolina")
x=iter(imie)
print(next(x))
print(next(x))
print(next(x))