menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(mayor)
print(menor)

lista = [43,32,12,76,43]
print(f"El mayor es {max(lista)} y el numero menor es {min(lista)}")


nombres = ['Juan','Pablo','Alicia','Carlos']
print(min(nombres))

nombre = "Carlos"
print(min(nombre))

nombre = "Carlos"
print(min(nombre.lower()))


dic = {'C1':45,'C2':11}
print(min(dic))

dic = {'C1':45,'C2':11}
print(min(dic.values()))

dic = {'C1':45,'C2':11}
print(min(dic.keys()))


lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros)- min(lista_numeros)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())