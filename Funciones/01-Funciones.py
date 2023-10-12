# def hola():
#     print("hola mundo!")
#     print("Ultimate Python!")


# hola()
# hola()


# def hola(nombre, apellido): #estos son parametros
#     print("Hola Mundo!")
#     print(f"Bienvenido {nombre}{apellido}")


# hola("Juan Carlos ", "Lopez") #estos dos son argumentos
# hola("Chanchito ", "Feliz")


# estos son parametros AQUI AGREGAMOS FUNCIONES CON PARAMETROS OPCIONALES
def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(f"Bienvenido {nombre}{apellido}")


hola("Juan Carlos ", "Lopez")  # estos dos son argumentos
hola("Chanchito ")


# YA CUANDO ESTAMOS MUY POR DEBAJO DE LA LINEA DE CODIGO PODEMOS NOMBRAR LOS ARGUMENTOS

hola(apellido="Obrador", nombre="Andres ")
