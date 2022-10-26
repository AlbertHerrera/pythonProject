import os
ruta = os.getcwd()
print(ruta)
ruta = os.chdir("C:\\Users\\Dragio The Wizard\\PycharmProjects\\pythonProject\\carpetaAlternativa")

archivo = open('OtroArchivo.txt')
print(archivo.read())

#La carpeta ya ha sido creada
#ruta = os.makedirs("C:\\Users\\Dragio The Wizard\\PycharmProjects\\pythonProject\\carpetaAlternativa\\otra_carpeta")

ruta = "C:\\Users\\Dragio The Wizard\\PycharmProjects\\pythonProject\\carpetaAlternativa\\OtroArchivo.txt"
elemento = os.path.basename(ruta)
carpeta = os.path.dirname(ruta)
separado = os.path.split(ruta)

print(f"El elemento es {elemento}, \n la carpeta es {carpeta}\n y el split es {separado}\n")

os.mkdir('C:\\Users\\Dragio The Wizard\\PycharmProjects\\pythonProject\\carpetaAlternativa\\testeliminar')
os.rmdir('C:\\Users\\Dragio The Wizard\\PycharmProjects\\pythonProject\\carpetaAlternativa\\testeliminar')


################################################################################################################

otro_archivo = open("C:\\Users\\Dragio The Wizard\\PycharmProjects\\pythonProject\\carpetaAlternativa\\otra_carpeta\\testmetodo2.txt")
print(otro_archivo.read())

################################################################################################################
from pathlib import Path

carpeta = Path('C:/Users/Dragio The Wizard/PycharmProjects/pythonProject/carpetaAlternativa/otra_carpeta')
archivo = carpeta / 'testmetodo2.txt'

mi_archivo = open(archivo)

archivo = Path('C:/Users/Dragio The Wizard/PycharmProjects/pythonProject/carpetaAlternativa/otra_carpeta')  / 'testmetodo2.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())