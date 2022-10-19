def suma(**kwargs):
    print(type(kwargs))
suma(x=3, y=5, z=2)


def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


print(suma(x=3, y=5, z=2))

def prueba(num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for arg in args:
        print(f"arg es igual a {arg}")
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(1,2,4,5,6,7,8,hola=1,adios=2,z="xd")

lista_args = [10,3,4,56,"oli"]
dic_kwargs = {'x': 1, 'y': 2}
prueba(1,2,*lista_args,**dic_kwargs)

def cantidad_atributos(*args,**kwargs):
    return len(args) + len(kwargs)

print(cantidad_atributos(1,2,3,4,5,6,"hola",z=1,x=2))

def lista_atributos(**kwargs):
    lista_valores = []
    for clave,valor in kwargs.items():
        lista_valores.append(valor)
    return lista_valores
print(lista_atributos(z=1,x=2))


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")
