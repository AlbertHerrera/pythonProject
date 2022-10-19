
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
    lista = list(cadena)
    lista_corta = []
    for n in lista:
        if n not in lista_corta:
            lista_corta.append(n)

    return sorted(lista_corta)
print(string_ordenar("holaa"))


#Ejercicio3
def pillar_al_cero(*args):
    for arg in args:
        index = args.index(arg)
        index_anterior = index - 1

        print(f"Este index es {index} con un valor de {arg} y el index anterior es {index_anterior} con un valor de {args[index_anterior]}")


        if arg == 0:
            if args[(args.index(arg))-1] == 0:
                return True
        else:
            pass
    return False


print(pillar_al_cero(40,50,0,0,60))

def pillar_al_cero2(*args):
    comprobar = {}
    for arg in args:
        comprobar[str(args.index)] = arg
    print(comprobar)
    return False


print(pillar_al_cero2(40,50,0,0,60))