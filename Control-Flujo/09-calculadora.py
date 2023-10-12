print("bienvenidos a la calculadora")
print("para salir escirbe salir")
print("las operaciones son suma, resta, divi y multi")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese primer numero: ")
        if resultado.lower() == "salir":
            break
    # print("Loop infinito")
    # break
        resultado = int(resultado)
    op = input("ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "divi":
        resultado /= n2
    else:
        print("Operacion no valida")

    print(f"El resultado es {resultado}")
