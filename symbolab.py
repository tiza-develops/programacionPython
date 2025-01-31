import sympy as sp
class funcionesContinuas:
    def __init__(self, expresion, dominio, codominio):
        self.expresion = expresion
        self.dominio = dominio
        self.codominio = codominio
        self.symbol = sp.symbols("x")
