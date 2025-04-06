###
# 04 - Listas Métodos
# Los métodos mas importantes para trabajar con listas
###

import os 
os.system("cls")

lista1 = ["a", "b", "c", "d"]

lista1.append("e") # Añade un elemento al final de la lista
lista1.insert(2,"@") # Añade un elemento en la posicion que quiera, primer argumento
# la posición, segundo elemento el elemento.
print(lista1)

lista1.extend(['w', 'z']) # Agrega elementos al final de la lista
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición del elemento que aparece en la lista.
print(lista1)

ultimo = lista1.pop() # Elimina el último elemento de la lista y además lo devuelve
print(lista1)
print(ultimo)

lista1.pop(1) # Elimina el segundo elemento de la lista
print(lista1)

# Eliminar a lo bestia
del lista1[-1]
print(lista1)

lista1.clear() # Elimina todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['hola', 'adiós', 'buenos días', 'Ana']
del lista1 [1:3]
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 4, 102, 23, 54, 67, 76]
numbers.sort() # Ordena la lista en orden ascendente
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 4, 102, 23, 54, 67, 76]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print('Ordenar listas de cadenas de texto (mezcla de mayusculas y minusculas)')
frutas = ['limon', 'Pera', 'Manzana', 'pera', 'manzana', 'Limon']
frutas.sort(key=str.lower)
print(frutas)

print('Ordenar listas de cadenas de texto (todo minuscula)')
frutas = ['limon', 'pera', 'manzana', 'pera', 'manzana', 'limon']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

#Más métodos útiles
animals = ['perro', 'gato', 'león', 'elefante', 'tigre', 'gato', 'tigre', 'perro']
print(len(animals))
print(animals.count('perro'))
print('perro' in animals) # Para saber si se encuentra el elemnto en la lista

print('\nEjercicios')
###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print('\nEjercicio 1')
lista1 = [1, 2, 3, 4, 5]
lista1.append(6)
lista1.insert(2, 10)
lista1[0]= 0
print(lista1)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print('\nEjercico 2')
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
lista_a.pop(3)
print(lista_a)
lista_b.clear()
print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print('\n Ejercicio 3')
lista_ejercicio_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista_ejercicio_3[2:5]
print(lista_ejercicio_3)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print('\nEjercicio 4')
lista_ejerccicio_4 = [5, 2, 8, 1, 9, 4, 2]
lista_ejerccicio_4.sort()
print(lista_ejerccicio_4)
print(lista_ejerccicio_4.count(2))
print(7 in lista_ejerccicio_4)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print('\n Ejercicio 5')
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(original)
print(copia_1)
print(copia_2)
print(referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print('\n Ejercicio 6')
lista_ejercico_6 = ["Manzana", "pera", "BANANA", "naranja"]
lista_ejercico_6.sort(key=str.lower)
print(lista_ejercico_6)