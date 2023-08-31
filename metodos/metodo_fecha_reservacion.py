import re


#### FUNCIONA PARA LA FECHA
def encontrar_fecha(mensaje):
    fecha_formato = r'\d{1,2} de [a-zA-Z]+'
    hora_formato = r'\d{1,2}(?::\d{2})?(?: ?(?:am|pm)|:\d{2})'

    fecha = re.findall(fecha_formato, mensaje)
    hora = re.findall(hora_formato, mensaje)
    fecha_completa = fecha.pop(0)
    hora = hora.pop(0)
    dia, de, mes = fecha_completa.split(" ")

    return dia, mes, hora
