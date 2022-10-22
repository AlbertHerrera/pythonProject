import random
from random import choice


def bienvenido():
    # Funcion que explica el juego y da la bienvenida al usuario:
    jugador = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                    "Hola, como te llamas?\n"
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"Bienvendio al juego del ahorcado, {jugador} -> ")

    return jugador


def elegir_palabra():
    # Funcion que elige una palabra de una lista al azar
    palabras = ["ANIMAL", "VETERINARIA", "CANIVALISMO", "MARIPOSA", "CLINICA",
                "OTORRINOLARINGOLOGO", "EDIFICACION", "METROPOLITANO", "ROSQUILLA",
                "BIGBLUE", "ASCENSOR", "CRUCIGRAMA", "MANIPULACION", "ESTRUCTURA"]
    palabra_secreta = random.choice(palabras)
    return palabra_secreta


def comprobar_letra(answer, palabra_secreta, letras_adivinadas):
    for l in palabra_secreta:
        if answer == l:
            letras_adivinadas.append(l)
            return letras_adivinadas
        else:
            pass
    restar_vidas()
    return letras_adivinadas


def resultado_actual(letras_adivinadas, palabra_secreta):
    # Cadena que devuelve que palabras tiene acertadas el usuario
    gui = []
    for l in palabra_secreta:
        if l not in letras_adivinadas:
            gui.append("-")
        else:
            gui.append(l)
    gui = " ".join(gui)
    if "-" not in gui:
        global ganador
        ganador = 1
        print(f"Has Ganado {jugador}!!!! y te han sobrado {vidas} vidas! {ganador}")
    return gui


def comprobar_ganador(palabra_secreta, palabra_jugador, jugador):
    if palabra_secreta == palabra_jugador:
        global ganador
        ganador = 1
        print(f"Has Ganado {jugador}!!!! y te han sobrado {vidas} vidas! {ganador}")

    else:
        restar_vidas()
        print(f"Has fallado {jugador}, te quedan {vidas} vidas!")


def restar_vidas():
    global vidas
    vidas -= 1


def siguiente_turno(jugador, vidas):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    answer = input(f"{jugador}, te quedan {vidas} vidas, porfavor elige una letra o adivina la palabra secreta:")
    answer = answer.upper()
    if len(answer) > 1:
        return {answer: 'palabra'}
    elif len(answer) == 1:
        return {answer: 'letra'}


vidas = 10
jugador = ''
gui = []
ganador = 0
answer = ''

jugador = bienvenido()
palabra_secreta = elegir_palabra()
letras_adivinadas = []
print(f"Hemos elegido una palabra secreta al azar, tienes {vidas} vidas para encontrar la respuesta \n"
      f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")


while vidas > 0 and ganador == 0:
    print(resultado_actual(letras_adivinadas, palabra_secreta))
    print(palabra_secreta)
    answer = siguiente_turno(jugador, vidas)

    for k, v in answer.items():

        if v == 'letra':
            comprobar_letra(k, palabra_secreta, letras_adivinadas)
        else:
            comprobar_ganador(palabra_secreta, k, jugador)
