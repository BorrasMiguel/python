###
# 01 - Expresiones regulares
###

"""
Las expresiones regulares son una secuencia de caracteres que forman un patron 
busqueda. Se utilizan para la busqueda de cadenas de texto, validación de datos... etc.

"""

"""
Por que aprender Regex?

- Búsuqeda avanzada: Encontrar patrones especificos en textos grandes de forma 
rápida y precisa.

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email
telefeno, ,etc.

- Manipulación del texto: Extraer, reemplazar y modificar partes de una cadena de texto.
"""

# 1. Importar el modulo de expresiones regulares
import re
# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
# 3. El texto donde queremos buscar
text = "Hola mundo"
# 4. Usar la función de busqueda de "re"
result = re.search(pattern, text)

if result:
    print("He encontrado el patrón en el texto")
else:
    print("No he encontrado el patrón de texto")

# .group() devuelve la cadena que coincide con el pattern
print(result.group()) # type: ignore

# .start() devolver la posición inicial de la coincidencia
print(result.start()) # type: ignore

# .end() devolver la posición final de la coincidencia
print(result.end()) # type: ignore

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la ocurrencia

text  = "Todo el mundo dice que la IA nos va a quitar el trbajo. Pero solo" \
"hace falta ver cómo la puede cagar con las Regex para ir con cuidado"

pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
    print(f"He encontrado el patrón en el texto, en la posición {found_ia.start()} y termina en la possición {found_ia.end()}")
else:
    print("No he encontrado el patrón")

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve  una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

find_all_python = re.findall(pattern, text)
print(len(find_all_python), find_all_python)

# Otro patrón 
text = "Me gusta Pyhhon. Pyxhon es lo máximo. Aunque Python no es tan dificil, ojo con Python"
pattern = "Py.hon"  # El punto quiere decir que busque cualquier caracter que haya ahi.

find_all_python = re.findall(pattern, text)
print(len(find_all_python), find_all_python)

# -------------------------
# .iter() devuelve un iterador que contienen todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# Ejercicio 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente
# Texto e indica en que posición empieza y termina la coincidencia 
# y cuantas veces se encontró

text = "Este es el curso de Python de midudev. Suscribete a midudev" \
"si te gusta este contenido! midu"

pattern = "midu"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())


# Modificadores: Opciones que se pueden agregar a un patrón para 
# cambiar su comportamiento

# re.IGNORECASE: Ignora las mayusculas y las minusculas
text  = "Todo el mundo dice que la IA nos va a quitar el trbajo. Pero la ia" \
"no es tan mala. Viva la IA"

pattern = "IA"
found_ia = re.findall(pattern, text, re.IGNORECASE)

if found_ia: print(found_ia)

# Ejercicio 03
# Encuantra todas las ocurrencias de la palabra python en el siguiente,
# texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso Python de midudev. ¡Suscribete a python"\
"si te gusta este contenido! PYTHON"

pattern = "python"

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)

### Remplazar el texto
# .sub(): Remplaza todas las coincidencias en un patrón de texto

text = "Hola, mundo Hola de nuevo"
pattern = "Hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)
    