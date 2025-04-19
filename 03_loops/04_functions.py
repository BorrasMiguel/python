###
# 04 - Funciones
# Bloques de código reutilizables
###


""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la funcion
    return valor_de_retorno # opcional

"""

# Ejemplo de una función para imprimir algo en consola
def saludar():
    print('Hola')

saludar()
saludar()

def saludar_a(nombre):
    print(f'Hola {nombre}')

saludar_a("Ana")
saludar_a("Miguel")
saludar_a("Bichofliya")

# Funciones con mas parametros
def sumar(a, b):
    suma = a + b
    return suma

result = sumar(2, 3)
print(result)

# Documentar las funciones con docstring
def restar(a, b):
    """Resta dos números y devuelve resultado"""
    return a - b

print(restar.__doc__)
help(restar)

# Parámetros por defecto
def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2))

# Argumentos por clave
def describir_persona(nombre, edad, sexo):
    print(f'Soy {nombre}, tengo {edad} años y me identifico como {sexo}')

# Los parametros son posicionales
describir_persona("miguel", 31, "gato")
describir_persona("hombre", "miguel", 31)

# Argumetos por clave
# Parámetros nombrados (Mucho mas recomendable esta opción)
describir_persona(sexo="gato", nombre="miguel", edad=31)

# Argumentos de longitud de variable (*args)
def sumar_numeros(*args):
    suma = 0
    for numeros in args:
        suma += numeros
    return suma

print(sumar_numeros(1, 2, 3, 4, 5, 6))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

print('\n')
mostrar_informacion_de(nombre="Miguel", edad=25, sexo="Hombre")
print('\n')
mostrar_informacion_de(nombre="Ana", edad=31, country="España")
print('\n')
mostrar_informacion_de(nombre="Siri", edad=3, es_gato=True, is_rich=True)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle

def multiplicacion(numero):
    for i in range(1, 11):
        print(f'{numero} * {i} = {numero * i}')

multiplicacion(5)
multiplicacion(20)

