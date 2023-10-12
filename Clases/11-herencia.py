class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):  # HERENCICIA
        print("Paseando")


perro = Perro()


class Chanchito(Perro):
    def programar(self):  # HERENCIA MULTINIVEL NO HACER A MAS DE DOS
        print("programando")


chanchito = Chanchito()
