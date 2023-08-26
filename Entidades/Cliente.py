class Cliente:
    __nombre = None
    __apellido = None
    __correo = None
    __id_reservacion = None

    # Insertamos el registro del cliente, antes debe de estar insertada el registro de reservacion
    def insercion_cliente(self):
        consulta = ('''INSERT INTO cliente(nombre, apellido, correo, id_reservacion1) VALUES ("{}","{}","{}",{})'''
                         .format(self.__nombre, self.__apellido, self.__correo, self.__id_reservacion))
        return consulta

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_correo(self, correo):
        self.__correo = correo

    def set_id_reservacion(self, id_reservacion):
        self.__id_reservacion = id_reservacion

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_correo(self):
        return self.__correo

    def get_id_reservacion(self):
        return self.__id_reservacion
