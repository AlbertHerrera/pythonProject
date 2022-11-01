def abrir_leer(documento):
    documento = open(documento, 'r')
    return documento.read()

def sobrescribir(doc):
    doc = open(doc, "w")
    doc.write("contenido eliminado")
    doc.close()
    return doc
