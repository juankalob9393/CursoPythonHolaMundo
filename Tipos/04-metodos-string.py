animal = "  chanCHito feliz "

print(animal.upper())
# upper() hace que el string de la variable animal hace que se haga en mayusculas"""
print(animal.lower())
# lower()  hace que el string de la variable animal hace que se haga en minusculas"""

print(animal.strip().capitalize())

# print(animal.capitalize())"""
# capitalize() toma el primer caracter de todo el string y lo hace en mayuscula"""


print(animal.title())
# title() transforma en mayuscula la primera letra de cada palabra del estring osea lo hace un titulo"""
print(animal.strip())
# strip() elimina espacio que esta a la izq y a la derecha"""

print(animal.lstrip())
# strip() elimina espacio que esta a la izq"""
print(animal.rstrip())
# strip() elimina espacio que esta a la derecha"""

print(animal.find("CH"))
# .find()  *en el parentesis va la cadena de caracteres a buscar* nos muestra el indice del o los caracteres que uno busca"""

print(animal.find("IT"))
# Aqui nos da -1 y ese significa * NO LO ENCONTRE * es cuando nos regresa un numero negativo
print(animal.replace("CH", "j"))
# .replace()  reemplaza la primera seleccion *CH* con la segunda seleccion *j* separados con *,*

print("CH" in animal)
# la funcion in nos da en booleano True o False si el caracter esta dentro del string de la variable animal, a diferencia de .find que nos da el numero del indice del caracter. la respuesta es True por que si esta CH en la variaable

print("CH" not in animal)
# Lo mismo que el in pero aqui se niega desde el inicio y resultado es False ya que decimos que no se encuentra pero si lo está por lo tanto es falso mi argumento
