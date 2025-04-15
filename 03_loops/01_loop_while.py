###
# 01 - Bucles (while)
###

# Permiten ejecutar un bloque de código repetidamente hasta que se cumpla una condición

import os
os.system('cls')

print('\n Bucle while')

# Bucle con una condición
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

# Utilizando la palabra break para romper el bucle infinito

contador = 0
while True:
    print('Este bucle es infinito')
    contador += 1
    if contador == 5: 
        print('Se acabó el bucle infinito')
        break # Sale del bucle

# Utilizando la palabra continue para saltar a la siguiente iteración
# y continuar con el bucle
print('\n Bucle continue')
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue # Salta a la siguiente iteración
    print(contador)   

# else
print('\n Bucle else')
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print('Se ha terminado el bucle')  # Para asegurarse que ha completado el bucle completo

# Ejercicio practico con while
# Pedirle a usuario un número que tiene que ser negativo 

# numero = -1
# while numero <= 0:
    # numero = int(input('Por favor, ingrese un número positivo: '))
    # if numero < 0:
        # print('El número ingresado no es positivo')
    

# Try except, evita que el código pete. Se encapsula la parte del código que puede generar problemas
numero = -1
while numero <= 0:
    try:
        numero = int(input('Por favor, ingrese un número positivo: '))
        if numero < 0:
            print('El número ingresado no es positivo')
    except:
        print('No has ingresado un número')
    

print(f'El número que has introducido es {numero}')


###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador = 10 
while contador > 0:
    print(contador)
    contador -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

contador = 1
numero = 0
while contador <= 20:
    if contador % 2 == 0:
        numero = numero + contador
    contador += 1

print(f'El resultado de la suma de números pares es: {numero}')

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
try:
    numero = int(input('Introduce un número entero positivo'))
except:
    print('No has introducido un número entero positivo')
numero_primero = numero
factorial = 1
while numero > 1:
    factorial *= numero

    numero -= 1

print(f'El factorial del número {numero_primero} es: {factorial}')

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
contraseña = str(input('\nIntroduce una contraseña de 8 al menos caracteres\n'))
check = False
while check == False:
    if len(contraseña) < 8:
        print('\nLa contraseña es demasiado corta, vuelve a introducirla')
        contraseña = str(input('\nIntroduce una contraseña de 8 al menos caracteres'))
    else:
        check = True
        print('Contraseña válida')

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
numero = int(input('Introduce un número entero positivo\n'))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f'{numero} x {contador} = {resultado}')
    contador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1

  