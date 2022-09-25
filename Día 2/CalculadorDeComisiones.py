comision = 13
def calcular_comision(dinero_total, comision):
    dinero = dinero_total * comision / 100
    dinero = round(dinero,2)
    return dinero

nombre = input("Como te llamas? ")
ventas = float(input("Cual es la cantidad de dinero que conseguiste este mes? "))
print(f"Hola {nombre}, te informamos que este mes vas a facturar un total de {calcular_comision(ventas,comision)} "
      f"euros este mes")