class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Pato(Volador, Nadador, Caminador):  # HERENCIA MULTIPLE
    def programar(self):
        print("programando")


pato = Pato()

pato.nadar()  # La herencia se aplica de derecha a izq.
