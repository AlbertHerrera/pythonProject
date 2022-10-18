def multiplicar (numero1, numero2):
    return numero1 * numero2

print(multiplicar(5,10))


def potencia(num1, num2):
    resultado = pow(num1, num2)
    return resultado

def usd_a_eur(dinero):
    usd = dinero
    euros_por_usd = 0.90
    euros = dinero * euros_por_usd
    return euros
dolares = 1000
euros = usd_a_eur(dolares)
print(euros)

def invertir_palabra(palabra):
    upper_string = palabra.upper()
    return upper_string[::-1]
palabra = "python"
palabra = invertir_palabra(palabra)
