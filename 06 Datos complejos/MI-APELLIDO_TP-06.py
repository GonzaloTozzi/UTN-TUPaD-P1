# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# frutas = list(precios_frutas.keys())
# print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# agenda = {}

# print("Carga contactos: ")
# for i in range(5):
#     nombre = input(f"Ingresa el nombre del contacto N°{i+1}: ")
#     numero = input(f"Ingresa el numero de {nombre}: ")
#     agenda[nombre] = numero

# print("Consulta de numero: ")
# buscar = input("Ingresa el nombre del contacto que queres buscar: ")

# if buscar in agenda:
#     print(f"El numero de {buscar} es: {agenda[buscar]}")

# else:
#     print(f"No se encontro el contacto {buscar}.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# frase = input("Ingresá una frase: ")

# palabras = frase.split()

# palabras_unicas = set(palabras)

# frecuencia = {}
# for palabra in palabras:
#     if palabra in frecuencia:
#         frecuencia[palabra] += 1
#     else:
#         frecuencia[palabra] = 1


# print("Palabras únicas:")
# print(palabras_unicas)

# print("Frecuencia de cada palabra:")
# for palabra, cantidad in frecuencia.items():
#     print(f"{palabra}: {cantidad}")


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# notasAlumnos = {}

# for i in range(3):
#     nombre = input(f"Ingresa el nombre del alumno {i+1}: ")

#     nota1 = float(input(f"Ingresa la primera nota de {nombre}: "))
#     nota2 = float(input(f"Ingresa la segunda nota de {nombre}: "))
#     nota3 = float(input(f"Ingresa la tercera nota de {nombre}: "))

#     notasAlumnos[nombre] = (nota1, nota2, nota3)

# print("\nPromedios de los alumnos: ")

# for nombre, notas in notasAlumnos.items():
#     promedio = sum(notas) / len(notas)
#     print (f"{nombre}: promedio = {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# parcial1 = {"Gonzalo", "Rober", "Pepe", "Carlos", "Lucia"}
# parcial2 = {"Gonzalo", "Carlos", "Pedro", "Rober"}

# ambos = parcial1 & parcial2

# solo_uno = parcial1 ^ parcial2

# al_menos_uno = parcial1 | parcial2

# print("Aprobados en ambos parciales:")
# print(ambos)

# print("\nAprobados solo en uno de los dos:")
# print(solo_uno)

# print("\nTotal de estudiantes que aprobaron al menos un parcial:")
# print(al_menos_uno)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.



# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.



# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.