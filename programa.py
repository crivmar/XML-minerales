from funciones import *

arbol=leer_documento("/home/crivero/Descargas/Git/XML-minerales/Minerals.xml")

m=0
while m!=6:
    m=menu()
    ## Ejercicio 1 ##
    if m==1:
        for i in listar_informacion(arbol):
            print(i)
            print(" ")
    ## Ejercicio 2 ##
    if m==2:
        for i,j in contar_informacion(arbol).items():
            print(i,":",j)
    ## Ejercicio 3 ##
    if m==3:
        print(filtro(arbol))

print("Fin del programa.")


