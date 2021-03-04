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
            print(i,":",int(j))
    # Ejercicio 3 ##
    if m==3:
        for i in filtro(arbol):
            print(" ")
            print(i)
    ## Ejercicio 4 ##
    if m==4:
        

print("Fin del programa.")


