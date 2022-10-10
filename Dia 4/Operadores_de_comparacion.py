mi_bool = 10 == 25
print(mi_bool)
mi_bool = 5+5 == 18-8
print(mi_bool)

mi_bool = 'blanco' == 'negro'
print(mi_bool)

num1 = 36
num2 = 17
mi_bool = num1>=num2

num1 = pow(25,0.5)
num2 = 5
mi_bool = num1 == num2

num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 < num3

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3


frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not ((palabra1 or palabra2) in frase)
print(mi_bool)