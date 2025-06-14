# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# def fact_num(num):
#     if num == 0 or num == 1:
#         return 1

#     else:
#         return num*fact_num(num -1)
    
# num = int(input("Ingrese un numero: "))

# print(fact_num(num))

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-2)+fibonacci(num-1)
    
# num = int(input("Ingrese un numero: "))

# print("Serie de Fibonacci hasta la posición", num, ":")
# for i in range(num + 1):
#     print(fibonacci(i), end=" ")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1). Prueba esta función en un algoritmo general.

# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia(base, exponente - 1)

# base = int(input("Introduce la base: "))
# exponente = int(input("Introduce el exponente: "))

# resultado = potencia(base, exponente)
# print(f"{base}**{exponente} = {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

# def decimal_a_binario(n):
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:
#         return decimal_a_binario(n // 2) + str(n % 2)

# numero = int(input("Introduce un número entero positivo: "))

# if numero >= 0:
#     binario = decimal_a_binario(numero)
#     print(f"El número {numero} en binario es: {binario}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# def es_palindromo(palabra):
#     if len(palabra) <= 1:
#         return True
#     if palabra[0] != palabra[-1]:
#         return False
#     return es_palindromo(palabra[1:-1])

# texto = input("Introduce una palabra sin espacios ni tildes: ").lower()

# if texto.isalpha():
#     if es_palindromo(texto):
#         print(f"{texto} es un palíndromo.")
#     else:
#         print(f"{texto} no es un palíndromo.")
# else:
#     print("Solo se permiten letras sin espacios ni tildes.")



# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# def suma_digitos(num):
#     if num < 10:
#         return num
#     else:
#         return num % 10 + suma_digitos(num//10)
    
# num = int(input("Ingrese un numero: "))
# print(suma_digitos(num))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

# def contar_bloques(n):
#     if n == 1:
#         return 1
#     else:
#         return n + contar_bloques(n-1)
    
# num = int(input("ingrese un numero: "))

# print(contar_bloques(num))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero//10, digito)
        else:
            return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese el digito que quiera contar: "))

print(contar_digito(numero, digito))
