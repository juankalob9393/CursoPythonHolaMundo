import math  # es un modulo incluido en python

# round redondea el numero mas cercano a al entero por ejemplo a 1.3 lo redondea a 1
print(round(1.3))
print(round(2.7))  # redondea a 3
print(round(3.9))  # redondea a 4
print(round(7.4))  # redondea a 7
# el valor absoluto lo regresa a positivo osea de -77 a 77
print(abs(-77))
print(abs(55))  # este al ser positivo lo deha como esta
print(math.ceil(1.6))  # lo lleva al numero entero mas cercano para arriba
print(math.floor(1.9999))  # lo lleva al numero entero mas cercano para abajo
# aqui nos muestra False ya que la funcion dice : no es un numero, pero al si ser un numero da false.
print(math.isnan(23))
# print (math.isnan ("23")) <----- este lanza un error ya que solo reconoce numeros no strings
print(math.pow(10, 3))  # eleva a una potencia osea 10 * 10 * 10  = 1000
print(math.sqrt(9))  # saca la raiz cuadrada de un numero
