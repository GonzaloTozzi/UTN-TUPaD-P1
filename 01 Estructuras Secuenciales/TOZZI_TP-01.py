import math

# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print ("Hola Mundo!")

# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
print(f"Hola, {nombre}!")

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = int(input("Por favor ingrese su edad: "))
residencia = input("Por favor ingrese su lugar de residencia: ")

print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = int(input("Ingrese el radio de la circunferencia: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El area de la circunferencia es {area}, y el perimetro es {perimetro}")

# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 60
minutos = segundos % 60

print(f"{segundos} segundos equivalen a {horas} horas y {minutos} minutos")

# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))

print(f"Tabla de multiplicar de {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


numero1 = int(input("Ingese el primer numero (distinto de Cero): "))
numero2 = int(input("Ingese el segundo numero (distinto de Cero): "))

suma = numero1 + numero2
resta = numero1 - numero2
multip = numero1 * numero2
divis = numero1 / numero2

print(f"{numero1} + {numero2} es {suma}")
print(f"{numero1} - {numero2} es {resta}")
print(f"{numero1} * {numero2} es {multip}")
print(f"{numero1} / {numero2} es {divis}")

# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

altura = float(input("Por favor ingrese su altura en metros: "))
peso = float(input("Por favor ingrese su peso en kilos: "))

imc = peso / altura ** 2

print(f"su indice de masa corporal es {imc}")

# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit

temp_cels = float(input("Ingrese una temperatura en grados celsius: "))

temp_fahr = 9/5 * temp_cels + 32

print(temp_fahr)

# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3)/ 3

print(f"El promedio entre{num1}, {num2} y {num3} es {promedio}")