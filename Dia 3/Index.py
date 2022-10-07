mi_texto = "Esta es una prueba"
resultado = mi_texto.index("prueba", 12,18)
print(resultado)

# Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
#
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado) 