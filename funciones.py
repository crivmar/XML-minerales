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

def contar_informacion(l):
    dic1={}
    for g in l.xpath("//information/group"):
        O=g.xpath('count(//information[group="Organic Minerals"])')
        Ar=g.xpath('count(//information[group="Arsenates"])')
        Sulf=g.xpath('count(//information[group="Sulfides"])')
        Sil=g.xpath('count(//information[group="Silicates"])')
        Pho=g.xpath('count(//information[group="Phosphates"])')
        Car=g.xpath('count(//information[group="Carbonates"])')
        Sulfa=g.xpath('count(//information[group="Sulfates"])')
        Hal=g.xpath('count(//information[group="Halides"])')
        Bor=g.xpath('count(//information[group="Borates"])')
        Ot=g.xpath('count(//information[group="Other"])')
        Ox=g.xpath('count(//information[group="Oxides"])')
        Nae=g.xpath('count(//information[group="Native Elements"])')

    dic1["Minerales Orgánicos"]=O
    dic1["Arseniatos"]=Ar
    dic1["Sulfuros"]=Sulf
    dic1["Silicatos"]=Sil
    dic1["Fosfatos"]=Pho
    dic1["Carbonatos"]=Car
    dic1["Sulfatos"]=Sulfa
    dic1["Haluros"]=Hal
    dic1["Boratos"]=Bor
    dic1["Otros"]=Ot
    dic1["Óxidos"]=Ox
    dic1["Elementos Nativos"]=Nae
    return dic1
    
# def filtro(l,t):
#     dic2={}
#     lita=[]
#     n=l.xpath('//information/[strunz="%i"]//name/text()'%t)
#     s=l.xpath("//information/strunz/text()")
#     # for i,j in zip(n,s):
#     #     dic2[i]=j.split(".")[0]
#     # print('''
#     # 1- Minerales elementos.
#     # 2- Minerales sulfuros y sulfosales.
#     # 3- Minerales haluros.
#     # 4- Minerales óxidos e hidróxidos.
#     # 5- Minerales carbonatos y nitratos.
#     # 6- Minerales boratos.
#     # 7- Minerales sulfatos.
#     # 8- Minerales fosfatos.
#     # 9- Minerales silicatos.
#     # 10- Compuestos orgánicos.
#     # ''')
#     # t=int(input("Introduce un numero del 1-10: "))
#     # while t<0 or t>10:
#     #     print("Error, debe ser un número del 1-10.")
#     #     t=int(input("Introduce un numero del 01-10: "))
#     # if t=1:
#     #     for i,j in dic2.items():
#     #         if j=="01":
                

#     return n