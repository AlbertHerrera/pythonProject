archivo = open('prueba.txt', 'w')
archivo.write('Soy el nuevo texto')
archivo.close()

archivo = open('prueba.txt', 'w')
archivo.writelines(['Hola ', 'Mundo'])
archivo.close()


archivo = open('prueba.txt', 'a')
archivo.write('\nBienvenido')
archivo.close()

archivo = open('mi_archivo','w')
archivo.write("Nuevo texto")
archivo.close()
archivo = open('mi_archivo','r')
print(archivo.read())

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())


un_texto = open('registro.txt', "a")
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for l in registro_ultima_sesion:
    un_texto.write(l+"\t")
un_texto.close()
un_texto = open("registro.txt", "r")
print(un_texto.read())
un_texto.close()