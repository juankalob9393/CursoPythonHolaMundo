print("bienvenidos a la calculadora de python a continuacion: ")

n1 = input("ingresa numero uno ")
n2 = input("ingresa numero dos ")

n1 = int(n1)
n2 = int(n2)

if n1 != 0 and n2 != 0:
    mensaje = "selecciona operacion"
    print(mensaje)

operacion = input(" ")


if operacion == "+":
    resultado = (n1 + n2)
elif operacion == "-":
    resultado = (n1 - n2)
elif operacion == "*":
    resultado = (n1 * n2)
elif operacion == "/":
    resultado = (n1 / n2)

mensaje = f""" 
Para los numeros {n1} y {n2}
el resultado de la operacion es {resultado}.
Si quieres hacer otra operacion corre de nuevo el programa.
"""
print(mensaje)
