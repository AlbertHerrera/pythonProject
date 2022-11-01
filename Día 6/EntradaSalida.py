remi_archivo = open('prueba.txt')
print(mi_archivo.read())
mi_archivo.close()
mi_archivo = open('prueba.txt')

print("*"*20)

una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea.rstrip())
una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()

print("*"*20)

mi_archivo = open('prueba.txt')
for l in mi_archivo:
    print("Aqui dice:"+ l)
mi_archivo.close()

print("*"*20)

mi_archivo = open('prueba.txt')
todas = mi_archivo.readlines()
print(todas)
mi_archivo.close()


un_texto = open('texto.txt')
#print(un_texto.read())
un_texto.close()

un_texto = open('texto.txt')
print(un_texto.readline())
un_texto.close()


un_texto = open('texto.txt')
todas = un_texto.readlines()
print(todas[1])
un_texto.close()





