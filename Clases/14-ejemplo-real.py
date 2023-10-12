class Model():

    table = False

    def __init__(self):
        if not self.table:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.table} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por ID {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)
