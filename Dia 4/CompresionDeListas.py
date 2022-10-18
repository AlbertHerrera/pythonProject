lista = list('hola')

print(lista)

string = "holas"
lista = [letra for letra in string]
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n  if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista)


pies = [10,20,30,40,50]
metros = [p *3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [pow(val,2) for val in valores]
print(valores_cuadrado)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [val for val in valores if val%2==0]

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temp-32)*(5/9) for temp in temperatura_fahrenheit]