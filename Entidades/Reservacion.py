
class Reservacion:
    def __init__(self, dia, mes, hora, no_personas):
        self.dia = int(dia)
        self.mes = mes
        self.hora = hora
        self.no_personas = int(no_personas)

    # La funcion primero verifica si en la base de datos no hay registro lleno
    def disponibilidad_reservacion(self):
        consulta = (
            '''SELECT a.id_reservacion FROM reservacion a WHERE a.dia ={} AND a.mes ="{}" AND a.hora ="{}" AND a.no_personas ={}'''
            .format(self.dia, self.mes, self.hora, self.no_personas))
        print(consulta)
        return consulta

    # Creamos una funcion para poder insertar registros a MYSQL
    def insercion_reservacion(self):
        query_reservacion = ('''INSERT INTO reservacion(dia, mes, hora, no_personas) VALUES ({},"{}","{}",{})'''
                             .format(self.dia, self.mes, self.hora, self.no_personas))
        print(query_reservacion)
        return query_reservacion

    # Buscaremos el id de la reservacion
    def busqueda_id_reservacion(self):
        query_id_reservacion = (
            '''SELECT a.id_reservacion FROM reservacion a WHERE a.dia = {} AND a.mes = "{}" AND a.hora = "{}" AND a.no_personas = {}'''
            .format(self.dia, self.mes, self.hora, self.no_personas))
        print(query_id_reservacion)
        return query_id_reservacion
