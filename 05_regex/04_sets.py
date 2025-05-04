import re
import os
os.system('cls')

# [: Coincide con cualquier carácter dentro de los corchetes
user_name = "rub.ius_69+"
pattern = r'^[\w._%+-]+$'
# ^$: Tiene que cumplir todo de principio a final
# +: Se puede repetir
match = re.search(pattern, user_name)
if match:
    print("El nombre de usuario es válido", match.group())
else:
    print("El nombre de usuario no es válido")

# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
match = re.findall(pattern, text)
print(match)

# Una Regex para encontrar las palabras man, fan, y ban
# pero ignora el resto

text = "man ran fan ñan ban"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Se complica el asunto, porque hay palabras que encajan pero no 
# empiezan por esas letras.
# Solo queremos palabras man , fan y ban

text = "omniman fanático man bandana"
# \b
pattern = r'\b[mfb]an|[mfb]an\b'
match = re.findall(pattern, text)
print(match)

# Rangos
# r'[a-z]'
# r'[A-Za-z0-9]

# [^]: Coincide con cualquier caracter que NO esté dentro de los 
# corchetes
text = "Hola mundo"
pattern = r'[^aeiou]' # Coincide con cualquier caracter que no este con los corchetes de dentro
matches = re.findall(pattern, text)
print(matches)