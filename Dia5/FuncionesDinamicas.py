

def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 345+234
resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_3_cifras_lista(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras_lista([556,99,600])
print(resultado)


def todos_positivos(lista):
    for n in lista:
        if n >= 0:
            pass
        else:
            return False
    return True


lista_numeros = [34, 354, 32, 1, -5, -575, -4]

