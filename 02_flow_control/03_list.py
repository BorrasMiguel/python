###
# 03 - Listas
# Secuencia mutable de elementos
# Pueden contener elementos de diferentes tipos.
###

import os
os.system("cls")

# Creación de listas
print("Crear listas")
lista = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # Lista de cadenas
lista3 = [1, "Hola", 3.14, True] # Lista de tipos


lista_vacia = []

lista_de_listas = [[1, 2], [2, 3], [4,5]]

print(lista)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista[0]) # Accede al primer elemento de la lista
print(lista2[1]) # Peras
print(lista2[-1]) # Plátanos

print(lista_de_listas[1][0]) # 2
print(lista_de_listas[2][1]) # 5

# Slicing de elementos
print("\nSlicing de listas")
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(lista1[2:4]) # [3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [3, 4, 5]
print(lista1[:]) # Te devuelve una copia

# Más
print(lista1[0:9:2]) # El último número nos indica el paso 
print(lista1[::2]) # Devuelve los indices pares de la lista
print(lista1[::1]) # Devuelve los indices impares de la lista
print(lista1[::-1]) # Devuelve índices inversos


# Modificar una lista

lista1[1] = 20
print(lista1[1])

# Agregar elementos a una lista
lista1 = [1, 2, 3]

# Forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# Forma corta y mas eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print(len(lista1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\n Ejercicio 1")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje2 = mensaje[7:]
print(mensaje2)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\n Ejercicio 2")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

print("\n Ejercicio 3")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan, ingredientes, pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("\n Ejercicio 4")
lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\n Ejercicio 5")
lista = [10, 20, 30, 40, 50]
print(lista[len(lista)//2])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("\n Ejercicio 6")
lista = [1, 2, 3, 4, 5, 6]
lista_reversa = lista[:(len(lista)//2)] 
print(lista_reversa[::-1] + lista[len(lista)//2:])

# Otra forma
print("\n Ejercicio 6")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista)//2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)