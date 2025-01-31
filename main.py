class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self): 
        return 3.14*self.radio**2

class Rectangulo:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def area(self):
        return l1 * l2
    def perimetro(self):
        return (l1*2)+(l2*2)

class Triangulo:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

class Pentagono:
    def __init__(self, l1, l2, l3, l4, l5):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
