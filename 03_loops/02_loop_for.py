###
# 02 - Bucle for
# Permiten ejecutar un bloque de código mientras itera un iterable o una lista
###

import os
os.system('clr')

print('\n Bucle for: ')

# Iterar una lista
frutas = ['manzana', 'pera', 'limón', 'mandarina']
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "Miguel"
for caracter in cadena:
    print(caracter)

# enumerate()
frutas = ['manzana', 'pera', 'limón', 'mandarina']
for index, fruta in enumerate(frutas):
    print(f'El indice es {index} y la fruta es {fruta}')

# Bucle anidados 
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f'{letra}{numero}')

# Break
animales = ['loro', 'gato', 'perro', 'ratón', 'pez', 'canario']
for idx,  animal in enumerate(animales):
    print(animal)
    if animal == 'ratón':
        print(f'El loro esta  escondido en el indice {idx}')
        break;

# continue
print('\n continue: ')
for idx,  animal in enumerate(animales):
    if animal == 'ratón':
        continue 
    print(animal)

# Comprensión de listas
animales = ['loro', 'gato', 'perro', 'ratón', 'pez', 'canario']
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)

#Muestra los numero pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9] if num % 2 == 0]
print(pares)









###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
numeros_pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] if num % 2 == 0]
print(numeros_pares)
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
    suma =+ numero
media = suma / len(numeros)
print(f'La media es: {media}')

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]  # Inicializamos con el primer elemento
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(f'El numero mayor es: {maximo}')
# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_largas)
# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input('\nIntroduce una letra').upper()
contador = 0
for palabra in palabras: 
    if palabra[0].upper() == letra:
        contador =+1

if contador > 0:
    print(f'Hay {contador} palabras que empiezan por esa letra')
else: 
    print(f'No hay ninguna palabra que empieze por la letra {letra}')

# for palabra in palabras:
#   if palabra.lower().startswith(letra):  # Comparamos en minúsculas
#     contador += 1
# print(f"Hay {contador} palabras que empiezan con la letra {letra}")