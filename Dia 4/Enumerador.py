lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice += 1

lista = ['a','b','c']
indice = 0
for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)


lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(type(mis_tuples))



lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]



for indice,nombre in list(enumerate(lista_nombres)):
    print(f'{nombre} se encuentra en el índice {indice}')

letras = list("Python")
lista_indices = list(enumerate(letras))


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice,nombre in list(enumerate(lista_nombres)):
    if nombre.startswith("M"):
        print(indice)
    else:
        pass