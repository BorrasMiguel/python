###
# 03 - range()
# Permite crear una secuencia o un rango de numeros
###
import os
os.system('clr')
print('\n range()')

# Genera  una secuencia de números del 0 al 9
# nums = range(10)
# for num in range(10):
#    print(num)

# Range(inicio, fin, paso)
# for num in range(0, 10, 2):
#     print(num)

for num in range(10, 0, -1):
    print(num)

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for num in range(1, 11):
    print(num)
# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for num in range(1, 21):
    if num  % 2 == 1:
        print(num)
# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for num in range(0, 51, 5):
    print(num)
# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for num in range(10, 0, -1):
    print(num)
# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0
for num in range(0, 101):
    suma += num
print(suma)
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("Introduce un número para la tabla de multiplicar: "))
for i in range(1, 11):
  print(f"{numero} x {i} = {numero * i}")