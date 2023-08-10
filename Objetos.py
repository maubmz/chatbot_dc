import mysql


class Reservacion:
    def __init__(self, dia, mes, hora, no_personas):
        self.dia = int(dia)
        self.mes = mes
        self.hora = hora
        self.no_personas = int(no_personas)

    # La funcion primero verifica si en la base de datos no hay registro lleno
    def disponibilidad_reservacion(self):
        consulta = ('''SELECT a.dia, a.mes, a.hora FROM reservacion a WHERE a.dia = {} AND a.mes = "{}" AND a.hora = "{} AND a.no_personas = {}"'''
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
        query_id_reservacion = ('''SELECT a.id_reservacion FROM reservacion a WHERE a.dia = {} AND a.mes = "{}" AND a.hora = "{}" AND a.no_personas = {}'''
            .format(self.dia, self.mes, self.hora, self.no_personas))
        print(query_id_reservacion)
        return query_id_reservacion

    # Actualizaremos la reservacion
    def update_reservacion(self):
        consulta = ('''UPDATE reservacion SET dia = {}, mes = "{}", hora = "{}", no_personas = {} WHERE id_reservacion = {}'''
                    .format(self.dia, self.mes, self.hora, self.no_personas))
        return consulta

    def tipo_valores_reservacion(self):
        print(type(self.dia))
        print(type(self.mes))
        print(type(self.hora))
        print(type(self.no_personas))

class Cliente:
    def __init__(self, nombre, apellido, correo, id_reservacion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.id_reservacion = int(id_reservacion)

    # Insertamos el registro del cliente, antes debe de estar insertada el registro de reservacion
    def insercion_cliente(self):
        query_cliente = ('''INSERT INTO cliente(nombre, apellido, correo, id_reservacion1) VALUES ("{}","{}","{}",{})'''
                         .format(self.nombre, self.apellido, self.correo, self.id_reservacion))
        print(query_cliente)
        return query_cliente



# Ingresamos los datos del mysql para su conexion con python
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='M1x_2021',
    database='cliente'
    )

