from mensajesOpenAi.extraccion_info import lineas_guia
from metodos.Metodo_Openai import get_datos


def datosa_lista(cadena):
    lista_elementos = cadena.split("[")
    lista_elementos = [elemento.rstrip(']') for elemento in lista_elementos if elemento]
    for elemento in lista_elementos:
        if elemento == "Ninguna":
            lista_elementos.remove("Ninguna")
            continue
    return lista_elementos


mi_texto = input("dame un texto: ")
# mi_texto = "quiero hacer una reservacion el 21 de marzo a las 14:00 a nombre de Miguel Herrera para 4 personas"
final_usuario = lineas_guia.format(mi_texto)
info = get_datos(final_usuario)
lista = datosa_lista(info)
print(info)
print(lista)
print(len(info))
print(type(info))
