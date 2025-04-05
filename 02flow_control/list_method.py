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