import turtle


class Zelva(turtle.Turtle):
    def __init__(self, nasobek):
        self.K = nasobek
        super().__init__()

    def forward(self, kolik):
        super().forward(self.K * kolik)

    pass


class Kreslic():
    def __init__(self):
        self.mojeZelvicka = turtle.Turtle()

    def forward(self, kolik):
        self.mojeZelvicka.forward(kolik)

    def left(self, kolik):
        self.mojeZelvicka.left(kolik)
    def speed(self, kolik):
        self.mojeZelvicka.speed(kolik)


zelva = Kreslic()
'''
for j in range(1, 10):
    #zelva = turtle.Turtle()
    zelva = Zelva(j)
    zelva.speed(0)
'''
zelva.speed(0)
for i in range(10):
    zelva.forward(100)
    zelva.left(150)
