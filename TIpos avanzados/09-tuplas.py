numeros = (1, 2, 3) + (4, 5, 6,)
print(numeros)
# LAS TUPLAS NO SE MODIFICAN

punto = tuple([1, 2])
print(punto)
# funcion tuple convierte las listas en tuplas

menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

# PARA MODIFICAR UNA TUPLA ES CREAR OTRA LISTA

listaNumeros = list(numeros)
print(listaNumeros)
