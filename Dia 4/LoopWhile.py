monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print("No tengo mas dinero")

respuesta = 's'
while respuesta == "s":
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")


while respuesta == "s":
    pass
else:
    print("Gracias")


nombre = input("Tu nombre")
for letra in nombre:
    if letra == "r":
        break
    print(letra)

nombre = input("Tu nombre")
for letra in nombre:
    if letra == "r":
        continue
    print(letra)

numero = 10
while numero >=0:
    print(numero)
    numero -= 1


numero = 50
while numero >=0:
    if numero%5 == 0:
        print(numero)
    else:
        pass
    numero -= 1
