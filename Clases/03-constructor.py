class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} con un {self.edad} año de edad dice : Guau!")


mi_perro = Perro("chanchito", 1)
mi_perro.habla()
