class Cliente:
    def __init__(self, nombre, apellido, id_reservacion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__id_reservacion = id_reservacion

    # Insertamos el registro del cliente, debe de estar insertado antes el registro de la reservacion
    def insercion_cliente(self):
        consulta = ('''INSERT INTO cliente(nombre, apellido, id_reservacion1) VALUES ("{}","{}",{})'''
                    .format(self.__nombre, self.__apellido, self.__id_reservacion))
        return consulta
