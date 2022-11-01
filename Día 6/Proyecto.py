from pathlib import Path
from os import system
def bienvenida():
    print("*"*50)
    nombre = input("Bienvenido a este gestor de recetas, \nCual es su nombre?\n")
    edad = input("Cual es tu edad?\n")
    system('cls')
    return nombre, edad

def directorio_base():
    base = Path("C:/Users/Usuario/pythonProject/Día 6/Recetas")
    return base

def total_recetas(base):
    recetas = []
    for txt in base.glob("**/*.txt"):
        recetas.append(txt)
    return len(recetas)

def leer_receta():
    #que categoria eliges
    # que receta quiere leer
    system('cls')
    base = directorio_base()
    dirs = []
    for dir in base.glob("*"):
        dirs.append(dir)
    print("*" * 50)
    print(f"Las categorias actuales són: \n")
    print(f"{dirs}")
    print("*" * 50)
    categoria = ''
    while categoria not in dirs:
        categoria = input(f"Porfavor elige una categoria valida:")
        categoria = categoria.capitalize()
    path_recetas = base / categoria
    recetas = []
    for txt in path_recetas.glob("*"):
        recetas = recetas.append(txt)
    print(f"Elige una receta de esta lista para leer: \n")
    print(f"{recetas}")
    while receta not in recetas:
        receta = input(f"Porfavor elige una receta para leer:")
        receta = receta.capitalize()
    leer = open(path_recetas / receta)
    return leer.read()

def crear_receta():
    #que categoria eliges
    #nombre y contenido
    return "crear_receta"

def crear_categoria():
    #Que nombre de categoria
    return "crear_categoria"

def eliminar_receta():
    #que categoria eliges
    # que receta quieres eliminar
    return "eliminar_receta"

def eliminar_categoria():
    return "eliminar_categoria"

def finalizar_programa():
    return "finalizar_programa"


siguiente = ''
num = ["1","2","3","4","5","6"]
election = "1"

while siguiente != 'n':
    #nombre, edad = bienvenida()
    nombre = "Albert"
    edad = 26
    print("*" * 50)
    print(f"Hola {nombre}, estas en mi gestor de recetas!")
    directorio = directorio_base()
    total = total_recetas(directorio)
    print(f"Actualmente las recetas se encuentran en: {directorio} \nHay un total de {total} recetas")
    print("*" * 50)
    siguiente = input("Escribe n para continuar: ")
    system('cls')
    print("*" * 50)

    cont = 1
    while cont == 1:
        while election != "6":
            election = input("""[1] - Leer receta
[2] - Crear receta
[3] - Crear categoría
[4] - Eliminar receta
[5] - Eliminar categoría
[6] - Finalizar programa
"""+"*"*50+"\n"+"Introduce un numero valido segun estas categorias:")
            system('cls')
            match election:
                case "1":
                    leer_receta()
                case "2":
                    print(crear_receta())
                case "3":
                    print(crear_categoria())
                case "4":
                    print(eliminar_receta())
                case "5":
                    print(eliminar_categoria())
                case "6":
                    print(finalizar_programa())
                case _:
                    print(f"No existe esa opcion! Porfavor {nombre}, elige una opcion valida")
        cont = 0



