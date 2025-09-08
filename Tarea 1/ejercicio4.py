class potencia:
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular_potencia(self):
        self.valor = self.base ** self.exponente
potencia_base = float(input("Ingrese la base: "))
potencia_exponente = float(input("Ingrese el exponente: "))
potencia1 = potencia(potencia_base, potencia_exponente)
potencia1.calcular_potencia()
print(f"El valor de la operacion es: {potencia1.valor}, con base {potencia1.base} y exponente {potencia1.exponente}")