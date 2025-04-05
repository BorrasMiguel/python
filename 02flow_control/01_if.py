### Senttencias condicionales

###importar modulo del sistema oprativo
import os
os.system("clear")

print("\n Sentencia simple condicional")
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")


edad = 15

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")


print("\n Sentencia simple condicional con else")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")
else:
    print("Eres menor de edad")


print("\n Sentencia simple condicional con elif")

nota = 7

if nota >= 9: 
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else: 
    print("Suspenso")

print("\n Condiciones multiples")
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("Policia")

condicion_especial = True

if edad >= 28 or condicion_especial:
    print("Puedes conducir")
else:
    print("Has tenido suerte")

### Darle la vuelta a la condición
es_fin_de_semana = False
if not es_fin_de_semana:
    print("No es fin de semana")


### No se recomienda, se recomiendo utilizar elif
print("Anidar condicionales")

edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir al cine")
    else:
        print("No tienes dinero para ir al cine")
else:
    print("Eres menor de edad")