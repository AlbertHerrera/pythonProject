from pathlib import Path

base = Path.home()
guia = Path(base , "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)
#################
print(guia.parent)
print(guia.parent.parent)
print(guia.parent.parent.parent)

##############################################################
base = Path("C:/Users/Dragio The Wizard/PycharmProjects/pythonProject/carpetaAlternativa")

guia = Path(base,"Europa")
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

guia = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)

from pathlib import Path
ruta_base = Path.home()
print(ruta_base)

##################################################################

"Curso Python"
"Día 6"
"practicas_path.py"
from pathlib import Path
ruta = Path("Curso Python", "Día 6", "practicas_path.py")
practicas = ruta.relative_to("Curso Python")
print(practicas)

###################################################################

from pathlib import Path
base = Path.home()
ruta = Path("Curso Python", "Día 6", "practicas_path.py")
ruta = Path(base,ruta)
print(ruta)