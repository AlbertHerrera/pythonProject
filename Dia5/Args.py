def suma(*args):
    return sum(args)

print(suma(5,6,4,6,87,8,))



def suma_cuadrados(*args):
    total = 0
    for arg in args:
        cuadrado = arg**2
        total += cuadrado
    return total

print(suma_cuadrados(1,2,3))

def suma_absolutos(*args):
    lista = []
    for arg in args:
        if arg < 0:
            arg = pow(pow(arg,2),0.5) #abs(arg)
            print(arg)
        lista.append(arg)
    return sum(lista)

print(suma_absolutos(1,2,3,4,-5))


def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"
