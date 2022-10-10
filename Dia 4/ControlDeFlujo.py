if 10 > 9:
    print('Es correcto')

x = True
if x:
    print('Es correcto')

if 5==2:
    print('No leo esto')
else:
    print('Esto si que lo leo')

mascota = 'conejo'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No sé qué animal tienes')
##
edad = 16
calificacion = 9
if edad < 18:
    print("Eres menor de edad")
    if calificacion >=5:
        print('Aprobado')
    else:
        print("No aprobado{¨´´´´.")
else:
    print('Eres Adulto')

num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
##
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
else:
    if tiene_licencia == False and edad >=18:
        print("No puedes conducir. Necesitas contar con una licencia")
    else:
        print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

##
habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles ==False and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == True and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")



