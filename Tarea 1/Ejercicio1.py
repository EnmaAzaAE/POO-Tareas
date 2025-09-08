class miembro:
    def __init__(self, nombre, edad = 0):
        self.nombre = nombre
        self.edad = edad
class familia:
    def __init__(self):
        self.juan =  miembro("juan")
        self.mama = miembro("mama")
        self.alberto = miembro("alberto")
        self.ana = miembro("ana")
    def edades(self,edad):
        self.juan.edad = edad
        self.alberto.edad = int((2/3)* edad)
        self.ana.edad =int( 4/3 * edad)
        self.mama.edad = int(self.juan.edad + self.alberto.edad + self.ana.edad)
edadjuan = int(input("Ingrese la edad de juan: "))
Familia = familia()
Familia.edades(edadjuan)
print(f"{Familia.juan.nombre} tiene {Familia.juan.edad} años"
      f"\n{Familia.alberto.nombre} tiene {Familia.alberto.edad} años"
      f"\n{Familia.ana.nombre} tiene {Familia.ana.edad} años"
      f"\n{Familia.mama.nombre} tiene {Familia.mama.edad} años")