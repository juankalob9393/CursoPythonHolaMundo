class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 5)


Perro.habla()

perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 5)
perro3 = Perro.factory()

print(perro3.edad, perro3.nombre)
