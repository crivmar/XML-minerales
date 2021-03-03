from funciones import *

arbol=leer_documento("/home/crivero/Descargas/Git/XML-minerales/Minerals.xml")

menu='''
1. Nombre e imagenes de los minerales.
2. Nº de minerales por grupo.
3. Clasificación Strunz.
4. Categoria mineral.
5. Elementos químicos.
6. Salir'''

opcion=int(input("Introduce un número de 1 al 5, 6 para salir: "))

while opcion!=:

    ## Ejercicio 1 ##
    if opcion=="1":
        for i in listar_informacion(arbol):
            print(i)
            print(" ")
    ## Ejercicio 2 ##

    print(menu)
    print(opcion)


