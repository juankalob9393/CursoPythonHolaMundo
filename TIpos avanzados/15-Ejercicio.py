from pprint import pprint

# ELIMINAR LOS ESPACIOS DE UN STRING

# string = "Hola mundo este es mi string"


# def quita_espacios(texto):
#     return [char for char in texto if char != " "]


# sin_espacios = quita_espacios(string)

# print(sin_espacios)


# CONTAR EN UN DICCIONARIIO CUANTOS CARACTERES SE REPITEN EN UN STRING

# string = "Hola mundo este es mi string"


# def quita_espacios(texto):
#     return [char for char in texto if char != " "]


# def cuenta_caracteres(lista):
#     chars_dict = {}
#     for char in lista:
#         if char in chars_dict:
#             chars_dict[char] += 1
#         else:
#             chars_dict[char] = 1
#     return chars_dict


# sin_espacios = quita_espacios(string)

# contados = cuenta_caracteres(sin_espacios)

# pprint(contados, width=1)


# ORDENAR LAS LLAVES DE UN DICCIONARIO POR EL VALOR QUE TIENEN Y DEVOLVER UNA LISTA QUE CONTIENE TUPLAS

# string = "Hola mundo este es mi string"


# def quita_espacios(texto):
#     return [char for char in texto if char != " "]


# def cuenta_caracteres(lista):
#     chars_dict = {}
#     for char in lista:
#         if char in chars_dict:
#             chars_dict[char] += 1
#         else:
#             chars_dict[char] = 1
#     return chars_dict


# def ordena(dict):
#     return sorted(
#         dict.items(),
#         key=lambda key: key[1],
#         reverse=True,
#     )


# sin_espacios = quita_espacios(string)

# contados = cuenta_caracteres(sin_espacios)

# ordenados = ordena(contados)

# print(ordenados)


# DE UN LISTADO DE TUPLAS DEVOLVER LAS TUPLAS QUE TENGAN EL VALOR MAYOR

# string = "Hola mundo este es mi string"


# def quita_espacios(texto):
#     return [char for char in texto if char != " "]


# def cuenta_caracteres(lista):
#     chars_dict = {}
#     for char in lista:
#         if char in chars_dict:
#             chars_dict[char] += 1
#         else:
#             chars_dict[char] = 1
#     return chars_dict


# def ordena(dict):
#     return sorted(
#         dict.items(),
#         key=lambda key: key[1],
#         reverse=True,
#     )


# def mayores_tuplas(lista):
#     maximo = lista[0][1]
#     respuesta = {}
#     for orden in lista:
#         if maximo > orden[1]:
#             break
#         respuesta[orden[0]] = orden[1]
#     return respuesta


# sin_espacios = quita_espacios(string)

# contados = cuenta_caracteres(sin_espacios)

# ordenados = ordena(contados)

# mayores = mayores_tuplas(ordenados)

# print(mayores)

# CREAR UN MENSAJE QUE DIGA LOS CARACTERES QUE MAS SE REPITEN SON:
# - C
# - D

string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacios = quita_espacios(string)

contados = cuenta_caracteres(sin_espacios)

ordenados = ordena(contados)

mayores = mayores_tuplas(ordenados)

mensaje = crea_mensaje(mayores)

print(mensaje)
