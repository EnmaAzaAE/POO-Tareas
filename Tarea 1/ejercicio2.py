class operacion:
    def __init__(self, numero1, numero2, suma):
        self.numero1 = numero1
        self.numero2 = numero2
        self.suma = suma

    def operacion(self):
        
        self.suma  = self.numero1 + self.suma 
        self.numero1 = self.numero1 + self.numero2**2
        self.suma = self.suma + self.numero1 / self.numero2
        return self.suma

    
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
suma = float(input("ingrese valor inicial de la suma: "))
operacion1 = operacion(numero1, numero2, suma)
print(f"El valor de la suma es: {operacion1.operacion()}")