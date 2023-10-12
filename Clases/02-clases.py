class Perro:
    def habla(self):  # metodos: funciones que se encuentran dentro de una clase y el primer parametro es siempre SELF
        print("Guau!")


mi_perro = Perro()
# print(type(mi_perro))

mi_perro.habla()

# aqui nos  muestra si mi_perro es de la clase Perro cmoo TRUE
print(isinstance(mi_perro, Perro))
