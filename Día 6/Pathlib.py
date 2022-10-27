from pathlib import Path, PureWindowsPath
#Con pathlib no hace falta abrir y cerrar
ruta = Path("C:/Users/Dragio The Wizard/PycharmProjects/pythonProject/carpetaAlternativa/otra_carpeta/testmetodo2.txt")

ruta_windows = PureWindowsPath(ruta)
print(ruta_windows)
print(ruta.read_text())
print(ruta.name)
print(ruta.suffix)
print(ruta.stem)


if not ruta.exists():
    print("Este archivo no existe")
else:
    print(f"El archivo {ruta.name} si existe")

