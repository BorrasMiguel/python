# 04 Variables

# Las variables sirven para guardar datos en la memoria

my_name = "Miguel"

print(my_name)

age = 30
print(age)

age = 40
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución, no tienes que declalarlo explicitamente.

name = "Miguel"
print(type(name))

name = 30 
print(type(name))

# tipado fuerte: no realiza conversiones de tipo automáticas

# print(10 + "2")


# f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age + 5} años")

# No recomendada forma de asignar variables
name, city, ciudad = "Miguel", 32, "Bogotá"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok"

# No usar camel case en python

# Python no tiene constantes por defecto
MI_CONSTANTE = 3.14 #UPPER_CASE -> CONSTANTES

is_usser_logged_in: bool = True  # Aqui bool sería como un comentario
print(is_usser_logged_in) # True

# is_usser_logged_in = 42
print(is_usser_logged_in)