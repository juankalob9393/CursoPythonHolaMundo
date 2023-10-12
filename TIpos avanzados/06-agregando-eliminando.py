mascotas = [
    "Asia",
    "Frijolito",
    "Lobezno",
    "Frijolito",
    "Lobezno",
    "copito",
    "Frijolito"
]
mascotas.insert(1, "Melvin")
mascotas.append("chanchito triste")

mascotas.remove("Frijolito")  # solo elimna el primer elemento que se intoduce
mascotas.remove("Frijolito")  # aqui se borra el 2do frijolito
mascotas.pop(1)  # este metodo elimina el indice 1
del mascotas[0]  # este tambien elimna el indice 0
mascotas.clear()  # este elimina todos los elementos del arreglos
print(mascotas)
