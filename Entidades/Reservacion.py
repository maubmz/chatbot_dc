from msilib.schema import Property


class Reservacion:
    __dia = None
    __mes = None
    __hora = None
    __no_personas = None

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

    def set_dia(self, dia):
        self.__dia = int(dia)

    def set_mes(self, mes):
        self.__mes = mes

    def set_hora(self, hora):
        self.__hora = hora

    def set_no_personas(self, no_personas):
        self.__no_personas = int(no_personas)

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_hora(self):
        return self.__hora

    def get_no_personas(self):
        return self.get_no_personas()