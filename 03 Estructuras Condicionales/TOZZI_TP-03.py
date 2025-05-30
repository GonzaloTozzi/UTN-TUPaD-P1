import random
from statistics import mode, median, mean

# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor ingrese su edad: "))

if edad>=18:    
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("Por favor ingrese su nota: "))

if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
    
else:
    print("Por favor, ingrese un numero impar")


# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
#   ● Niño/a: menor de 12 años.
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Por favor ingrese su edad: "))

if edad < 12:
    print("Niño/a")

elif edad >= 12 and edad < 18:
    print("Adolscente")

elif edad >= 18 and edad < 30:
    print("Adulto/a joven")

else:
    print("Adulto")  

#  Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contraseña = input("Por favor ingrese una contraseña que tenga entre 8 a 14 caracteres: ")

if len(contraseña) <=14 and len(contraseña) >= 8:
    print("Ha ingresado una contraseña correcta")

else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")

elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")

elif media == mediana and mediana == moda:
    print("Sin sesgo")

# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input("Por favor ingrese una frase: ")

if frase.lower()[-1] in "aeiou":
    frase = frase + "!"
    print(frase)

else:
    print(frase)



# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.


nombre = input("Primero ingrese su nombre: ")

menu = input("Seleccione una opcion\n1 Si quiere su nombre en mayusculas \n2 Si quiere su nombre en minusculas\n3 Si quiere su nombre con la primer letra en mayusculas ")

if menu == "1":
    print(nombre.upper())

elif menu == "2":
    print(nombre.lower())

elif menu == "3":
    print(nombre.title())

else:
    print("Opcion invalida")

# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

nivel = int(input("Ingrese la magnitud del terremoto (en numeros): "))

if nivel < 3:
    print('"Muy leve" (imperceptible)')

elif nivel >= 3 and nivel < 4:
    print('"Leve (ligeramente perceptible)')

elif nivel >= 4 and nivel < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños)')

elif nivel >= 5 and nivel < 6:
    print('"Fuerte" (puede causar daños en estructuras debiles)')

elif nivel >= 6 and nivel < 7:
    print('"Muy fuerte" (puede causar daños significativos)')

elif nivel >= 7:
    print('"Extremo" (puede causar graves daños a gran escala)')

else:
    print("Ingrese un valor valido")



# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

def obtener_estacion(hemisferio, mes, dia):
    if hemisferio.upper() not in ['N', 'S']:
        return "Hemisferio no válido. Usa 'N' para norte o 'S' para sur."

    # Convertimos el mes y día a un número de fecha para facilitar comparaciones
    fecha = (mes, dia)

    if hemisferio.upper() == 'N':
        if (3, 20) <= fecha <= (6, 20):
            return "Primavera"
        elif (6, 21) <= fecha <= (9, 22):
            return "Verano"
        elif (9, 23) <= fecha <= (12, 20):
            return "Otoño"
        else:
            return "Invierno"
    else:  # Hemisferio Sur
        if (3, 20) <= fecha <= (6, 20):
            return "Otoño"
        elif (6, 21) <= fecha <= (9, 22):
            return "Invierno"
        elif (9, 23) <= fecha <= (12, 20):
            return "Primavera"
        else:
            return "Verano"

hemisferio = input("En que hemisferio se encuentra? (N/S): ")
mes = int(input("Que mes es?: "))
dia = int(input("Que dia es?: "))

estacion = obtener_estacion(hemisferio, mes, dia)

print(f"Estas en {estacion}") 


