import math
class circulo:
    def __init__(self, radio):
        self.radio = radio

    def formulas(self):
        self.area = math.pi * (self.radio ** 2)
        self.perimetro = 2 * math.pi * self.radio
circulo_radio = float(input("Ingrese el radio del circulo: "))
circulo1 = circulo(circulo_radio)
circulo1.formulas()
print(f"El area del circulo es: {circulo1.area}")
print(f"El perimetro del circulo es: {circulo1.perimetro}")