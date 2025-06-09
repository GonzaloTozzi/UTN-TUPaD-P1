# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

print(saludar_usuario(input("Cual es tu nombre? ")))

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")
edad = input("Cuantos años tienes? ")
residencia = input("Donde vives? ")

informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#  calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    return print(f"El area es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2*radio*3.14
    return print(f"El perimetro es {perimetro}")

radio = int(input("Ingrese el radio del circulo "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas= segundos/3600
    return print(f"{segundos} segundos son: {horas} horas")

segundos = float(input("Ingrese los segundos "))
segundos_a_horas(segundos)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}")

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    if b != 0:
        division = a/b
    else:
        division= "division por cero"
    
    return print(f"Suma: {suma}\nResta: {resta}\nMultiplicacion: {multiplicacion}\nDivision: {division} ")

a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))

operaciones_basicas(a,b)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso/ (altura**2)
    return print(f"Tu IMC es: {imc:.2f}")

peso = float(input("Ingrese su peso en Kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

calcular_imc(peso, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahr = (celsius * 9/5) + 32
    return print(f"{celsius} grados celsius son: {fahr:.2f} grados fahrenheit")

celsius = float(input("Ingrese la temperatura en grados celsius: "))
celsius_a_fahrenheit(celsius)


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a,b,c):
    promedio = (a+b+c)/3
    return print(f"El promedio entre {a}, {b} y {c} es: {promedio}")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

calcular_promedio(a,b,c)
