###
# 04 - Diccionarios
# Los diccionarios son colecciones de clave-valor
# Sirven para almacenar datos relacionados
###

import os
os.system('clr')

# Ejemplo de diccionario
persona = {
    "nombre": "miguel",
    "edad": 31,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "@miguel",
        "instagram": "@miguel",
        "linkedin": "Miguel Borrás"
    }
}

# Para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# Para cambiar valores al acceder
persona["nombre"] = "ana"
persona["calificaciones"][2] = 10
print(persona["nombre"])
print(persona["calificaciones"][2])

print(persona)

# Eliminar completamente una propiedad 
del persona["edad"]
print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f'es_estudiante: {es_estudiante}')
print(persona)

# Sobreescribir un diccionario con otro diccionario
a = {"name": "miguel", "age": 25}
b = {"name": "ana", "es_estudiante": True}

a.update(b)
print(a)

# Comprobar si exite un valor
print("nombre" in persona) # True
print("name" in persona) # False

# Obtener todas las claves
print("\nKeys")
print(persona.keys())

# Obtener todos los valores
print("\nValues")
print(persona.values())

# Obtener tanto clave como valor
print("\nItems")
print(persona.items())

for key, value in persona.items():
    print(f'{key}: {value}')