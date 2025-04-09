# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
numero = int(input('Introduce un número entero positivo\n'))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f'{numero} x {contador} = {resultado}')
    contador += 1
