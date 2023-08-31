from msilib.schema import Property


class Reservacion:

    def __init__(self, dia, mes, hora, no_personas):
        self.__dia = dia
        self.__mes = mes
        self.__hora = hora
        self.__no_personas = no_personas

    def print_reservacion(self):
        return f"Impresion de la reservacion {self.__dia}, el mes {self.__mes}, a las {self.__hora} con {self.__no_personas}"

    # La funcion hace una consulta a la base de datos que nos tendra que regresar el id de la reservacion
    def id_reservacion(self):
        consulta = (
            '''SELECT a.id_reservacion FROM reservacion a WHERE a.dia ={} AND a.mes ="{}" AND a.hora ="{}" AND a.no_personas ={}'''
            .format(self.__dia, self.__mes, self.__hora, self.__no_personas))
        return consulta

    # Metodo que inserta el registro de la reservacion a MYSQL
    def insercion_reservacion(self):
        consulta = ('''INSERT INTO reservacion(dia, mes, hora, no_personas) VALUES ({},"{}","{}",{})'''
                    .format(self.__dia, self.__mes, self.__hora, self.__no_personas))
        return consulta
