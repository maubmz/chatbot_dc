def texto_lista(cadena):
    lista_elementos = cadena.split("[")
    lista_elementos = [elemento.rstrip(']') for elemento in lista_elementos if elemento]
    return lista_elementos
