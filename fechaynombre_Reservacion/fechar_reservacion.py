import re

#### FUNCIONA PARA LA FECHA
'''
mensaje = input("A que hora sera la reservacion?  ")

date_pattern = r'\d{1,2} de [a-zA-Z]+'
time_pattern = r'\d{1,2}(?::\d{2})?(?: ?(?:am|pm)|:\d{2})'

dates = re.findall(date_pattern, mensaje)
times = re.findall(time_pattern, mensaje)

print("Fechas encontradas:", dates)
print("Horas encontradas:", times)
'''



class Fecha_Reservacion:
    dates = None
    times = None

    def encontrar_fecha(self, mensaje):
        date_pattern = r'\d{1,2} de [a-zA-Z]+'
        time_pattern = r'\d{1,2}(?::\d{2})?(?: ?(?:am|pm)|:\d{2})'
        dates = re.findall(date_pattern, mensaje)
        times = re.findall(time_pattern, mensaje)
        return dates, times
