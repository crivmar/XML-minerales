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
    dic1["Minerales Orgánicos"]=l.xpath('count(//information[group="Organic Minerals"])')
    dic1["Arseniatos"]=l.xpath('count(//information[group="Arsenates"])')
    dic1["Sulfuros"]=l.xpath('count(//information[group="Sulfides"])')
    dic1["Silicatos"]=l.xpath('count(//information[group="Silicates"])')
    dic1["Fosfatos"]=l.xpath('count(//information[group="Phosphates"])')
    dic1["Carbonatos"]=l.xpath('count(//information[group="Carbonates"])')
    dic1["Sulfatos"]=l.xpath('count(//information[group="Sulfates"])')
    dic1["Haluros"]=l.xpath('count(//information[group="Halides"])')
    dic1["Boratos"]=l.xpath('count(//information[group="Borates"])')
    dic1["Otros"]=l.xpath('count(//information[group="Other"])')
    dic1["Óxidos"]=l.xpath('count(//information[group="Oxides"])')
    dic1["Elementos Nativos"]=l.xpath('count(//information[group="Native Elements"])')
    return dic1
    
def filtro(l):
    print('''
    1- Minerales elementos.
    2- Minerales sulfuros y sulfosales.
    3- Minerales haluros.
    4- Minerales óxidos e hidróxidos.
    5- Minerales carbonatos y nitratos.
    6- Minerales boratos.
    7- Minerales sulfatos.
    8- Minerales fosfatos.
    9- Minerales silicatos.
    10- Compuestos orgánicos.
    ''')
    t=int(input("Introduce un numero del 1-10: "))
    while t<0 or t>10:
        print("Error, debe ser un número del 1-10.")
        t=int(input("Introduce un numero del 1-10: "))
    if t==1:
        g=l.xpath('//information[starts-with(strunz,"01")]/../name/text()')
    elif t==2:
        g=l.xpath('//information[starts-with(strunz,"02")]/../name/text()')
    elif t==3:
        g=l.xpath('//information[starts-with(strunz,"03")]/../name/text()')
    elif t==4:
        g=l.xpath('//information[starts-with(strunz,"04")]/../name/text()')
    elif t==5:
        g=l.xpath('//information[starts-with(strunz,"05")]/../name/text()')
    elif t==6:
        g=l.xpath('//information[starts-with(strunz,"06")]/../name/text()')
    elif t==7:
        g=l.xpath('//information[starts-with(strunz,"07")]/../name/text()')
    elif t==8:
        g=l.xpath('//information[starts-with(strunz,"08")]/../name/text()')
    elif t==9:
        g=l.xpath('//information[starts-with(strunz,"09")]/../name/text()')
    elif t==10:     
        g=l.xpath('//information[starts-with(strunz,"10")]/../name/text()')      
    return g

def informacion_rel(l):
    print('''
    1- Organic.
    2- Arsenate.
    3- Sulfide.
    4- Inosilicate.
    5- Silicate.
    6- Nesosilicate.
    7- Phosphate.
    8- Carbonate.
    9- Sulfate.
    10- Halide.
    11- Borate.
    12- Tellurite.
    13- Sodalite.
    14- Tectosilicate.
    15- Oxide.
    16- Vanadate.
    17- Sulfate.
    18- Native.
    19- Phyllosilicate.
    20- Tungstate.
    21- Molybdate.
    22- Sorosilicate.
    ''')
    t=input("Introduce una categoría de las aparecidas o unas cuantas letras: ")
    n=l.xpath('//information[category[contains(text(),"%s")]]/../name/text()'%t)
    return n

def elemen_qui(l):
    t=input("Introduce un elemento de la tabla periódica (p.e: Pb (Plomo),Si (Silicio), Ca (Calcio)): ")
    n=l.xpath('//information[formula[contains(text(),"%s")]]/../name/text()'%t)
    f=l.xpath('////formula[contains(text(),"%s")]//text()'%t)
    return n