class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} con un {self.edad} año de edad dice : Guau!")


Perro.patas = 3
mi_perro = Perro("chanchito", 1)
mi_perro.patas = 5
mi_perro2 = Perro("Felipe", 2)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
