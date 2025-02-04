class cuadro:
    def __init__ (self, lado):
        self.lado = lado
        self.area = lado**2
        self.peri = lado*4
        print(self.area)
        print(self.peri)

cuadro(2)
