
#Ejercicio1
def devolver_distintos(num1,num2,num3):
    lista_numeros = [num1,num2,num3]
    suma_total = sum(lista_numeros)
    if suma_total > 15:
        return max(lista_numeros)
    elif suma_total < 10:
        return min(lista_numeros)
    elif suma_total >=10 and suma_total <=15:
        lista_numeros.pop(lista_numeros.index(max(lista_numeros)))
        lista_numeros.pop(lista_numeros.index(min(lista_numeros)))
        return lista_numeros[0]
print(devolver_distintos(1,2,10))

#Ejercicio2
def string_ordenar(cadena):

    #Los sets ya quitan los duplicados
    #for letra in cadena:
        #mi_set.add(letra)
    lista = list(cadena)
    lista_corta = []
    for n in lista:
        if n not in lista_corta:
            lista_corta.append(n)

    return sorted(lista_corta)
print(string_ordenar("holaa"))


#Ejercicio3
# def pillar_al_cero(*args):
#     for arg in args:
#         index = args.index(arg)
#         index_anterior = index - 1
#
#         print(f"Este index es {index} con un valor de {arg} y el index anterior es {index_anterior} con un valor de {args[index_anterior]}")
#
#
#         if arg == 0:
#             if args[(args.index(arg))-1] == 0:
#                 return True
#         else:
#             pass
#     return False
#
#
# print(pillar_al_cero(40,50,0,0,60))
#
# def pillar_al_cero2(*args):
#     comprobar = {}
#     for arg in args:
#         print(type(args.index(arg)))
#         comprobar[args.index(arg)] = arg
#     print(comprobar)
#     return False
#
#
# print(pillar_al_cero2(40,50,0,0,60))


def pillar_al_cero3(*args):
    cadena = str(args)
    if "0, 0," in cadena:
        return True
    else:
        return False

def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador]== 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1
    return False
print(ceros_vecinos(40,50,0,0,60))


def contar_primos(num1):
    contador_primo = 2
    lista_primos = []
    while contador_primo < num1:
            contador2 = 1
            regla = 0
            while contador2 <= contador_primo:
                if contador_primo % contador2 == 0:
                    regla +=1
                    contador2 +=1
                else:
                    contador2 +=1
            if regla > 2:
                contador_primo +=1
            else:
                lista_primos.append(contador_primo)
                contador_primo +=1
    return lista_primos


print(contar_primos(5000))
