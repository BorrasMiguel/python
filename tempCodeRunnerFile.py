numero = -1
while numero <= 0:
    try:
        numero = int(input('Por favor, ingrese un número positivo: '))
        if numero < 0:
            print('El número ingresado no es positivo')
    except:
        print('No has ingresado un número')
    

print(f'El número que has introducido es {numero}')