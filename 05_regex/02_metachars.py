###
# 02- Meta carácteres
# Los metacarácteres son símbolos especiales con significados
# específicos en las expresiones regulares.
###
import os
os.system('clr')
import re



# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la"
matches = re.findall(pattern, text)

print(matches)

text = "casa caasa cosa cesa cisa causa"
pattern = "c.sa"
matches = re.findall(pattern, text)
print(matches)

# --------------------------
text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la"
matches = re.findall(pattern, text)

print(matches)

# ----------------------------
# Encontrar solo el punto. La barra invertida anula el significado de los metachars
text = "Mi casa es blanca. Y el coche es negro"
pattern = r"\."  # Cancela el significado especial del punto
matches = re.findall(pattern, text)

print(matches)


# \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es el 123456789"
found = re.findall(r'\d{9}', text)

print(found)

# Ejercicio: detectar d¡si hay un numero de España en el texto
# gracias al prefijo +34

text = "Mi número de teléfono es +34 688999999 apuntalo vale?"
pattern = r'\+34 \d{9}'
found = re.search(pattern, text)

if found:
    print(f"Encontre el número de telefono {found.group()}")
else:
    print("No se ha encontrado un número de teléfono válido")

# \w: Coincide con cualquier caracter alfanumérico (a-z, A-Z, 0-9)
text = "el_rubius_69"
pattern = r'\w'
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blanco (espacio, tabulación, salto de linea)
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r'\s'
found = re.findall(pattern, text)
print(found)

# ^: Coincide con el extremo de una cadena
usuer_name = "@432_name"
pattern = r'^\w' # Validar nombre de usuario. Esto quiere decir que el principio de la cadena de texto no sea un símbolo
valid = re.search(pattern, usuer_name)

if valid:
    print("El nombre de usuario es valido")
else:
    print("El nombre de usuario no es válido")

phone = "+345 698999000"
pattern = r'^\+\d{2,3} ' # Dejo un espacio para que lo tenga en cuenta.
valid  = re.search(pattern, phone)
if valid: 
    print("El número de teléfono es válido")
else:
    print("El número de teléfono no es válido")

# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r'mundo$'
valid = re.search(pattern, text)

if valid: 
    print("La cadena es válida")
else:
    print("La cadena no es válida")

# Ejercicio 
# Valida que un correo sea valido de gmail

email = "miguel@gmail.com"
pattern = r'^w+@gmail.com$' # Que empiece con un caracter alfanumérico una o mas veces y que termine con @gmail.com
valid = re.search(pattern, email)
if valid: 
    print("El correo es válido")
else:
    print("El correo no es valido")


# Ejercicio:
# Tenemos una lista de archivos, necesitamos saber los nombres 
# de los ficheros con extensión .txt

files = "file1.txt file2.pdf midu-of.webp secret.txt"
name_files = r'\b[\w\d._%]+\.txt\b'
result = re.findall(name_files, files)

print(result)

# \b: Coincide con el principio o final de una palabra
text = "casa casado casada cosa cosas"
pattern = r'\bc.sa\b'
found = re.findall(pattern,text)
print(found)

# |: Coincidir con una opción u otra
text = "platano, manzana, aguacate, palta, pera"
pattern = r"palta|aguacate|p..a"

matches = re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b" # En el caso de que exista antes de una b una a, quiero que me la devuelvas
matches = re.findall(pattern, text)
print(matches)

# Ejercicio
# Haz opcional que aparezca un  +34 en el siguiente texto
phone = "+34 699888555"
pattern = r'\+?|34 \d{9}' 
matches = re.findall(pattern, phone)
print(matches)

# {n}: Exactamente n veces
text = "aaaaaa      aa        aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)

# {n, m}: De n a m veces
text  = "u uu uuu u"
pattern = "u{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Encientra las palabras de mas de 4 a 6 letras
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{5,6}\b"  # \b: detecta las palabras
matches = re.findall(pattern, words)
print(matches)

# Ejercicio: Encuentra las palabras de mas de 6 letras
words = "ala fantástico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"  # \b: detecta las palabras
matches = re.findall(pattern, words)
print(matches)