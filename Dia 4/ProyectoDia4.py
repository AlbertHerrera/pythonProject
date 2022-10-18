from random import *
numero_secreto = randint(0,100)
intentos = 0
nombre = input("Dime tu nombre:")
print(f"Hola {nombre}, he pensado un número entre 0 y 100 \nTienes 8 intentos para adivinarlo")
while intentos < 8:
    numero_usuario = int(input(f"Cuál es el número?"))
    intentos += 1
    if numero_usuario > 100 or numero_secreto < 0 or type(numero_secreto) != int:
        print("Porfavor, elige un numero entre 0 y 100")
        intentos -= 1
        continue
    if numero_usuario > numero_secreto:
        if numero_usuario > numero_secreto+25:
            print("Uff es muchisimo menos! (-25)")

        else:
            print("Uff Casi lo tienes, un poco menos!")

    if numero_usuario < numero_secreto:
        if numero_usuario < numero_secreto-25:
            print("Uff es mucho mas! (+25)")
        else:
            print("Uff Casi lo tienes, un poco mas!")
    if numero_usuario == numero_secreto:
        print(f"Felicidades, {nombre} has adivinado el numero secreto con un total de {intentos} intentos")
if numero_usuario != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")
