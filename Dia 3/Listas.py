# Práctica Listas 1
# Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
mi_lista = ["a",True,3, 4.5,"lol"]

# Práctica Listas 2
# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#
# medios_transporte = ["avión", "auto", "barco", "bicicleta"]

# No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir
# un nuevo elemento.
medios_transporte = ["avión", "auto", "barco", "bicicleta"]

medios_transporte.append("motocicleta")

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)