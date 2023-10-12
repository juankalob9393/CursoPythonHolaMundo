# numero = 1
# duplicar el numero constante mente

# while numero < 100:
#     print(numero)
#     numero *= 2

# literal primero el valor inicial de numero es 1, despues evalua si es menor a 100 pasa a imprimir
# luego lo multiplica por dos y ese es el numero valor de numero, vuelve a evaluar si es menor a 100
# y como es menor, lo muliplica por 2 y ese es el nuevo valor de numero eso lo hace hasta que este sea menor a 100
# la ultima iteracion llega a 64, al momento de duplicarlo evalua si es menor a 100 pero es 128 y como no lo es
# no lo imprime y solo llega hasta 64

# comando = ""
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)
# AQUI SE AGREGA COMANDO.LOWER para poder dar a conocer al programa si es mayusculas o minusculas el comando


while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break

# esto es un LOOP
