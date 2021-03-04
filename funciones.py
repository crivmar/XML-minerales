from lxml import etree

def menu():
    print('''
    1. Nombre e imagenes de los minerales.
    2. Nº de minerales por grupo.
    3. Clasificación Strunz.
    4. Categoria mineral.
    5. Elementos químicos.
    6. Salir
    ''')
    opcion=int(input("Elige una opción: "))
    print("-"*40)
    while opcion<1 or opcion>6:
        print("Error")
        opcion=int(input("Elige una opción: "))
    return opcion

def leer_documento(d):
    with open(d) as f:
        l=etree.parse(d)
    return l

def listar_informacion(l):
    n=l.xpath("//name/text()")
    u=l.xpath("//image/text()")
    for i in range (len(n)):
        n[i]=n[i]+","+" "+"puedes ver su imagen en: " +u[i]
    return n

# def contar_informacion(l):
#     n=l.xpath("//information/group/text()")