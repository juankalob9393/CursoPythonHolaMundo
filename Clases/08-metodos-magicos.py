class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def __del__(self):
        print(f"Chao perro :( {self.nombre}")

    def habla(self):
        print(f"{self.nombre} dice Guau!")


perro = Perro("chanchito", 7)
del perro
