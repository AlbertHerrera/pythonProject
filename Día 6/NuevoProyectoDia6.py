import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(),"Documentos/GitHub/pythonProject/Día 6/Recetas")



def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


#Mostrar menu inicio
def inicio():
    system('clear')
    print('*'*50)
    print('*'*5+" Bienvenido al administrador de recetas "+ '*'*5)
    print('*'*50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")
    
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print('''
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear categoría
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Finalizar programa
        ''')
        eleccion_menu = input()
        return (eleccion_menu)
inicio()

def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categorias(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista)+1):
        eleccion_correcta = input("\n Elige una categoria: ")

    return lista[int(eleccion_correcta)-1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] -  {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

menu = 0
if menu == 1:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categorias(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    #elegir recetas
    #leer receta
    #Volver al inicio
    pass

elif menu ==2:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categorias(mis_categorias)
    #Crear receta nueva
    #Volver al inicio
    pass

elif menu == 3:
    #Crear categoria
    #Volver al inicio
    pass
elif menu == 4:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categorias(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    #Elegir recetas
    #Eliminar receta
    #Volver inicio
    pass

elif menu == 5:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categorias(mis_categorias)
    #eliminar categoria
    #Volver al inicio
    pass
elif menu == 6:
    pass


