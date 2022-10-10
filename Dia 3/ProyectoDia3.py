#Primero ingresa un text
#Ingresa 3 letras a tu eleccion
#5 tipos de analisis

#1 Cuantas veces aparecen cada letras a eleccion, ponerlas en listas y contar las letras en cada lista, asegurarse de ponerlo a minisculas
#2 Cuantas palabras hay en to do el texto
#3 Cual es la primera letra del texto y cual es la ultima
#Como quedaria el texto si invirtieramos el orden de las palabras
#5 La palabra python esta dentro del texto?

my_string = input("Ingresa el texto que desea analizar:")
letras_clave = input("ingresa las 3 letras clave:")
#Pasamos los valores a minuscula

my_string = my_string.lower()
letras_clave = letras_clave.lower()

#1

letras_clave = letras_clave.replace(" ","")
lista_claves = list(letras_clave)

my_string_sin_espacios = my_string.replace(" ","")
lista_letras = list(my_string_sin_espacios)

print("------------------.\n")
print(f"Análisis numero 1")
print(f"Analizando texto con las letras clave: {lista_claves[0]},{lista_claves[1]} y {lista_claves[2]}")
print(f"Se han encontrado un total de: {lista_letras.count(lista_claves[0])} coincidencias para la letra clave: {lista_claves[0]} \nSe han encontrado un total de: {lista_letras.count(lista_claves[1])} coincidencias para la letra clave: {lista_claves[1]} \nSe han encontrado un total de: {lista_letras.count(lista_claves[2])} coincidencias para la letra clave: {lista_claves[2]}")

#2
print("------------------.\n")
total_palabras = my_string.split(" ")
print(f"Análisis numero 2")
print(f"Contando las palabras del texto")
print(f" Hay un total de : {len(total_palabras)} palabras")

#3
print("------------------.\n")
print("Análisis numero 3")
print("La primera letra de tu texto es:")
print(list(my_string_sin_espacios)[0].upper())
print("La ultima letra de tu texto es:")
print(list(my_string_sin_espacios)[-1])

#4
print("------------------.\n")
print("Análisis numero 4")
total_palabras = my_string.split(" ")
total_palabras.reverse()
texto_reves = " ".join(total_palabras)
print(f"Tu texto al revés: \n {texto_reves}")

#5
print("------------------.\n")
print("Análisis numero 5")
print(f"Esta la palabra 'python' en tu texto?: {'python' in my_string }")
