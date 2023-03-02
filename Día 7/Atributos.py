class Pajaro:
    #Atributo de clasee
    alas = True
    #Atributos de instancia
    def __init__(self, parametro, especie):
        self.atributo = parametro
        self.especie = especie

mi_pajaro = Pajaro('atributo','Tucan')  
palabra = 'hola'
print(mi_pajaro.atributo)
mi_pajaro.atributo = 'verde'
print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.atributo}")

print(Pajaro.alas)
print(mi_pajaro.alas)