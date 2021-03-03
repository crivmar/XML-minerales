from funciones import *

arbol=leer_documento("/home/crivero/Descargas/Git/XML-minerales/Minerals.xml")

## Ejercicio 1 ##

for i in listar_informacion(arbol):
    print(i)
    print(" ")