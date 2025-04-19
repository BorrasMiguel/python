"""
En jurasic park, se ha observado que los dinosaurios carnivoros, como el T.Rex, 
depositan un número par de huevos. Imagina que tienes una lista de números
enteros en la que cada número representa la cantidad de huevos puestos por un
dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnivoros (T-Rex)
aquellos numeros que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros 
y devuelva la suma total de los huevos que pertenecen a los dinosaurios 
carnivoros (es decir, la suma de todos los números pares en la lista).
"""

def count_carinivore_dinosaur_eggs(egg_list) -> int:
    """
    Esta función recibe una lista de numeros enteros que representa la cantidad de huevos que han puesto 
    diferentes dinosaurios en el parque jurásico y los de número par son carnivoros.
    Devuelve un número con la suma de todos los huevos carnivoros.
    """
    total_carinivores_eggs = 0
    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs
    return total_carnivore_eggs


