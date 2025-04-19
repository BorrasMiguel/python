"""
Esta en equilibrio la alianza entre Reed Richards y Johnny Strom?

En el universo de los 4 fantasticos, la unión y el equilibrio entre los 
poderes es fundamental para enfrentar cualquier desafio. En este problema,
nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La antorcha humana), representado por la letra J.

Objetivo:
Crea una función en python que reciba una cadena de texto. Esta función debe 
contar cuantas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza 
entre la mente y el fuego esta en equilibrio y la funcion debe retornar True

- Si las cantidades no son iguales, la función debe retornar False

- En el caso de que no aparezca ninguna de las dos letras en la
cadena, se entiende de que el equilibrio se mantiene (0=0), por lo que 
la función debe retornar True.
"""

def check_is_balanced(text):
    text = text.upper()

    # contar facilmente el numero de veces que aparece una letra
    count_r = text.count("R")
    count_j = text.count("J")

    print(f'count_r: {count_r}, count_j: {count_j}')
    
    return count_j == count_r
    

print(check_is_balanced("rrrrjjj"))