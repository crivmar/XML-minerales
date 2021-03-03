from lxml import etree

def leer_documento(d):
    with open(d) as f:
        l=etree.parse(d)
    return l

def listar_informacion (l):
    n=l.xpath("//name/text()")
    u=l.xpath("//image/text()")
    for i in range (len(n)):
        n[i]=n[i]+","+" "+"puedes ver su imagen en: " +u[i]
    return n

