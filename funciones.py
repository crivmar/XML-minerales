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
    O=0
    Ar=0
    Sulf=0
    Sil=0
    Pho=0
    Car=0
    Sulfa=0
    Hal=0
    Bor=0
    Ot=0
    Ox=0
    Nae=0
    n=l.xpath("//information/group/text()")
    for i in n:
        if i=='Organic Minerals':
            O+=1
            dic1["Minerales Orgánicos"]=O
        elif i=='Arsenates':
            Ar+=1
            dic1["Arseniato"]=Ar
        elif i=='Sulfides':
            Sulf+=1
            dic1["Sulfuros"]=Sulf
        elif i=='Silicates':
            Sil+=1
            dic1["Silicatos"]=Sil
        elif i=='Phosphates':
            Pho+=1
            dic1["Fosfatos"]=Pho
        elif i=='Carbonates':
            Car+=1
            dic1["Carbonatos"]=Car
        elif i=='Sulfates':
            Sulfa+=1
            dic1["Sulfatos"]=Sulfa
        elif i=='Halides':
            Hal+=1
            dic1["Haluros"]=Hal
        elif i=='Borates':
            Bor+=1
            dic1["Boratos"]=Bor
        elif i=='Other':
            Ot+=1
            dic1["Otros"]=Ot
        elif i=='Oxides':
            Ox+=1
            dic1["Óxidos"]=Ox
        elif i=='Native Elements':
            Nae+=1
            dic1["Elementos Nativos"]=Nae
                    
    return dic1
    
