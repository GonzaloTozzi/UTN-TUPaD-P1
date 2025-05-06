import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print (i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = str(input("Ingrese un numero para saber cuantos digitos tiene: "))
print(len(numero))


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero:"))

for i in range(primer_numero+1,segundo_numero):
    print(i)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero = int()
numero_usuario = ""
while numero_usuario != 0:
    numero_usuario = int(input("Ingrese un numero: "))
    numero += numero_usuario

print(numero)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_aleatorio = str(random.randint(0,9))
respuesta = ""
intentos = 0

while respuesta != numero_aleatorio:
    respuesta = str(input("Ingrese un numero: "))
    intentos += 1

print(f"Necesito {intentos} intentos para adivinar el numero")



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

techo = int(input("Ingrese un numero: "))
suma = 0
for i in range(0, techo+1):
    suma += i

print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numero = 0
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
for i in range(100):
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

    if numero % 2 == 0:
        contador_pares += 1
    elif numero % 2 != 0:
        contador_impares += 1
    
print(f"Hay {contador_pares} numeros pares\n{contador_impares} numeros impares \n{contador_positivos} numeros negativos\n{contador_negativos} numeros negativos")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0
numero = 0
contador = 0

for i in range(10):
    numero = int(input("Ingrese un numero: "))
    suma += numero
    contador += 1


print(f"La media de la suma de los valores es {suma/contador}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un número: ")
numero_invertido = numero[::-1]

print("Número invertido:", numero_invertido)
