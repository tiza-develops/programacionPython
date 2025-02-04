class cuadro:
    def __init__ (self, lado):
        self.lado = lado
        self.area = lado**2
        self.peri = lado*4
        return "Perímetro"

cuadro(4)
