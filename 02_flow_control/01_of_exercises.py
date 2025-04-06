###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1, num2 = input("Introduce dos números al azar: ").split()

if num1 > num2:
    print(f"El primer numero es mayor que el segundo")
elif num1 < num2:
    print(f"El segundo numero es mayor que el primero")
else:
    print("Los dos números son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\n Ejercicio 2")
num1 = float(input("\n Introduce el primer número: "))
num2 = float(input("\n Introduce el segundo número: "))
operacion = input("\n Introduce la operación (+, -, *, /): ")


if operacion == "+":
    print(f"El resultado de la suma es: {float(num1) + float(num2)}")
elif operacion == "-":
    print(f"El resultado de la resta es: {float(num1) + float(num2)}")
elif operacion == "*":
    print(f"El resultado de la multiplicación es: {float(num1) * float(num2)}")
elif operacion == "/":
    if num2 == 0:
        print("No se puede dividir por cero")
    else:
        print(f"El resultado de la división es: {float(num1) / float(num2)}")
else: 
    print("Operación no válida")

# Ejercicio 3: Año bisiestoº
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\n Ejercicio 3")
anno = int(input("Introduce un año: "))

if (anno % 4 == 0 and anno % 100 != 0) or anno % 400 == 0:
    print(f"El año {anno} es bisiesto")
else:
    print(f"El año {anno} no es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\n Ejercicio 4: ")
edad = int(input("Introduce tu edad: "))
if edad >= 0 and edad <= 2:
    print("Eres un bebe")
elif edad >= 3 and edad <= 12:
    print("Eres un niño")
elif edad >= 13 and edad <= 17:
    print("Eres adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres adulto")
elif edad >= 65:
    print("Eres un anciano")
else:
    print("Edad no valida")
