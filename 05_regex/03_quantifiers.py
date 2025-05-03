###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias
# de un carácter o grupo de caracteres se deben encontrar en una cadena
###

import re

# *: Puede aparecer 0 o mas veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1: 
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?


# +: Una a más veces.
text = "dddd aaa ccc bb a casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)