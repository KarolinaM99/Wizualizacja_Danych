class Kwadrat():
    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self):
        return 4*self.x+4*self.x

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

    
kw=Kwadrat(5)
print(kw.__add__())