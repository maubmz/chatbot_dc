class Cliente:
    def __init__(self, nombre, apellido, correo, id_reservacion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.id_reservacion = id_reservacion

    # Insertamos el registro del cliente, antes debe de estar insertada el registro de reservacion
    def insercion_cliente(self):
        query_cliente = ('''INSERT INTO cliente(nombre, apellido, correo, id_reservacion1) VALUES ("{}","{}","{}",{})'''
                         .format(self.nombre, self.apellido, self.correo, self.id_reservacion))
        print(query_cliente)
        return query_cliente

