'''
author: Hugo Tonatiuh Carrillo Bonilla
date: Feb 26, 2025
'''
class Cuenta:
    def __init__(self, saldo, tipo, propietarix):
        self.saldo = saldo
        self.tipo = tipo
        self.propietarix = propietarix

def imprimirDetallesCuenta(persona):
    print("Saldo:", persona.saldo, "Tipo", persona.tipo, "Propietarix", persona.propietarix)

def retirar():
    message = input("Indique cuánto desea retirar")
    try:
        persona.saldo = persona.saldo - message
        print("Su nuevo saldo es", persona.saldo)
    except:
        print("Introduzca un número")
        retirar()

def depositar():
    message = input("Indique cuánto desea depositar")
        try:
            persona.saldo = persona.saldo - message
            print("Su nuevo saldo es", persona.saldo)
        except:
            print("Introduzca un número")
            retirar()


