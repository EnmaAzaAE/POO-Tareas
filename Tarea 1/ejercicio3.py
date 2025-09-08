class salario:
    def __init__(self, retencion, horas_trabajadas, valor_hora):
        self.retencion = retencion
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        self.bruto = self.horas_trabajadas * self.valor_hora
        self.neto = self.bruto - (self.bruto * self.retencion / 100)
        self.retencion_valor = self.bruto * self.retencion / 100
retencion = float(input("Ingrese el porcentaje de retencion: "))
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))
salario1 = salario(retencion, horas_trabajadas, valor_hora)
salario1.calcular_salario()
print(f"El salario bruto es: {salario1.bruto}")
print(f"El valor de la retencion es: {salario1.retencion_valor}")
print(f"El salario neto es: {salario1.neto}")
        