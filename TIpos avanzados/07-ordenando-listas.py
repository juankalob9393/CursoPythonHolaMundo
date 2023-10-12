numeros = [12, 58, 8, 4, 69, 22, 9, 14, 48,]

# numeros.sort() #de mayor a menor

# numeros.sort(reverse=True) #de menor a mayor


numeros2 = sorted(numeros, reverse=True)
# esta funcion crea una nueva lista, no modifca la existente como .sort
# y tambien podemos hacer que los acomode al reves con reverse =True

print(numeros)
print(numeros2)


usuarios = [
    [4, "chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]
usuarios.sort()
print(usuarios)


usuarios2 = [
    ["chanchito", 7],
    ["Felipe", 8],
    ["Pulga", 6]
]


def ordena(elemento):
    return elemento[1]
# usuarios2.sort() # SOLO SI EL PRIMER ELEMENTO ES ALGO ORDENABLE SI LO ORDENA pero hay que indicarle a SORT como acomodarlo


# aqui le ddcimos que argumento toma parapoder acomodar la lista de arriba osea el indice 1
# usuarios2.sort(key=ordena)

# print(usuarios2)

# para LA FUNCION LAMBDA y ahorrarnos
# la def ordena(elemento):
#     return(elemento[1])
# usamos:
usuarios.sort(key=lambda el: el[1])
print(usuarios)
