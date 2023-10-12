# Set significa grupo o conjunto
# conexion de datos que no se puede repetir y no esta ordenada
primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)


segundo = [3, 4, 5]
segundo = set(segundo)

# TAMBIEN PODEMOS HACER UNA !!! UNION !!! DE DOS SETS:

# print(primer | segundo)  #union
# ELIMINA LOS VALORES REPETIDOS ENTRE AMBOS SETS

# print(primer & segundo)  #interseccion
# este regresa los valores que estan dentro de AMBOS SETS

# print(primer - segundo)  # diferencia
# muestra solamente los datos que estan en el conjunto de la izq y se quitan los que estan a la derecha

print(primer ^ segundo)  # diferencia simetrica
# elimina los numeros que estan en ambos sets  y muestra los que no

if 5 in segundo:
    print("hola mundo")
