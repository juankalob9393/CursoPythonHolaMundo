mascotas = ["Asia", "Lobezno", "Frijolito", "Copito"]
# print(mascotas[0])
# para cambiar un elemento del listado=

mascotas[0] = "Bicho"
# print(mascotas)
# # print(mascotas[0:3])  # aqui manda solo 3 elementos
# print(mascotas[:3])  # si eleminamos el elemento de la izq python
# # lo toma como 0
# # y aqui sin el indice derecho lo toma hasta la longitud final del listado
# print(mascotas[2:])
# print(mascotas[-1])  # asi va al revez de derecha a izq
# al hacer esto le decimos, toma el primer elemento, salta el 2do y toma el 3ro y salta el 4to

numeros = list(range(21))
print(numeros[::2])  # pares
print(numeros[1::2])  # impares
