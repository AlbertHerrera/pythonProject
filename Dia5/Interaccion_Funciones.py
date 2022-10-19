from random import *
#Lista Inicial
palitos = ['-','--','---','----']
#Mezclar Palitos
def mezclar(lista):
    shuffle(lista)
    return lista
#Pedirle intento
def probar_suerte():
    intento =''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)
#Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado el palito {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
intento = probar_suerte()
resultado = chequear_intento(palitos_mezclados,intento)

###########################################################
def lanzar_dados():
    num1 = randint(1,6)
    num2 = randint(1,6)
    return num1,num2
def evaluar_jugada(num1,num2):

    suma_dados = num1+num2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados >6 and suma_dados<10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >=10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

num1,num2 = lanzar_dados()
print(evaluar_jugada(num1,num2))


#################
lista_numeros = [1,2,15,7,2]
def reducir_lista(lista):
    lista_reducida = []
    for n in lista:
        if n not in lista_reducida:
            lista_reducida.append(n)
    numero_maximo = max(lista_reducida)
    lista_reducida.pop(lista_reducida.index(numero_maximo))
    return lista_reducida

def promedio(lista_corta):
    num = 0
    for n in lista_corta:
        num = num +n
    promedio = num / len(lista_corta)
    return promedio

lista_c = reducir_lista(lista_numeros)
print(lista_c)
print(promedio(lista_c))


#########################################
lista_numeros = [1,2,15,7,2]
def lanzar_moneda():
    lista = ["Cara","Cruz"]
    return choice(lista)

def probar_suerte(moneda,lista_numeros):
    if moneda == 'Cara':
        print("La lista se autodestruirá")
        lista_numeros = []
        return lista_numeros
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista_numeros
print(probar_suerte(lanzar_moneda(),lista_numeros))