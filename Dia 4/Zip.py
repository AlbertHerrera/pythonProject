nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
combinados = list(zip(nombres,edades))
print(combinados)

nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']
combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

my_tuple = list(zip(capitales,paises))
for capital,paises in my_tuple:
    print(f"La capital de {paises} es {capital}")

marcas = ['puma','addidas','nike']
productos =['Pantalones','Sudadera','Bambas']

mi_zip = zip(marcas,productos)



espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol,portugues,ingles))
