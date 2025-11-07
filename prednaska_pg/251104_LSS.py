class Prvek:
    def __init__(self, x , dalsi):
        self.x = x
        self.dalsi = dalsi

seznam = None

seznam = Prvek(10, None)
druhy = Prvek(20, None)
seznam.dalsi = druhy

p = seznam
while p != None:
    print(p.x)
    p = p.dalsi