###
# 02 Booleanos
# Valores logicos: True y False
# Fundamentos para el control de flujo y la lógica de programación.

#Los booleanos representan valores de verdad: True o False

import os
os.system("clear")


print("\nBooleanos básicos")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano
print("\nOperadores de comparación")
print("5 > 3", 5 > 3)    #True
print("5 < 3", 5 < 3)    #False
print("5 == 5", 5 == 5)    #True
print("5 != 5", 5 != 5)    #False

print("\n Comparar candenas de texto")
print("manzana < pera:", "manzana" < "pera") #true compara letra a letra.
print("'Hola' == 'hola'", "Hola" == "hola")


#TablaS de verdad
print("\nTablas de verdad")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)



numero = 0

if numero: # False
    print("Aqui no entrará nunca")

nombre = ""
print("El nombre no es vacio")

numero = 3
es_el_tres = numero == 3 # comparación

if es_el_tres:
    print("El número es el tres")


print("\n La condición ternaria")
# Forma concisa de hacer un if else
# Codigo si cumple la condición if condicion else codigo que no cumple

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)