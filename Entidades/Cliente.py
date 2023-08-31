class Cliente:
    def __init__(self, nombre, apellido, correo, id_reservacion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__id_reservacion = id_reservacion

    # Insertamos el registro del cliente, antes debe de estar insertada el registro de reservacion
    def insercion_cliente(self):
        consulta = ('''INSERT INTO cliente(nombre, apellido, correo, id_reservacion1) VALUES ("{}","{}","{}",{})'''
                         .format(self.__nombre, self.__apellido, self.__correo, self.__id_reservacion))
        return consulta


