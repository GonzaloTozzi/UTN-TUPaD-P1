import random
from statistics import mode, median, mean

# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Por favor ingrese su edad: "))

# if edad>=18:    
#     print("Es mayor de edad.")
# else:
#     print("Es menor de edad.")

# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota = int(input("Por favor ingrese su nota: "))

# if nota>=6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = int(input("Ingrese un numero par: "))

# if numero % 2 == 0:
#     print("Ha ingresado un numero par")
    
# else:
#     print("Por favor, ingrese un numero impar")


# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
#   ● Niño/a: menor de 12 años.
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Por favor ingrese su edad: "))

# if edad < 12:
#     print("Niño/a")

# elif edad >= 12 and edad < 18:
#     print("Adolscente")

# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")

# else:
#     print("Adulto")  

#  Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contraseña = input("Por favor ingrese una contraseña que tenga entre 8 a 14 caracteres: ")

# if len(contraseña) <=14 and len(contraseña) >= 8:
#     print("Ha ingresado una contraseña correcta")

# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)

# if media > mediana and mediana > moda:
#     print("Sesgo positivo o a la derecha")

# elif media < mediana and mediana < moda:
#     print("Sesgo negativo o a la izquierda")

# elif media == mediana and mediana == moda:
#     print("Sin sesgo")

# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

