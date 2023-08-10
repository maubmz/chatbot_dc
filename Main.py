import mysql.connector

from Entidades.Reservacion import Reservacion
from Entidades.Cliente import Cliente

# Ingresamos los datos del mysql para su conexion con python
connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='M1x_2021',
        database ='cliente'
    )

# Comprobamos si la conexion a la base de datos fue exitosa
if connection.is_connected():
        print("Nos conectamos pibe vamoo")
cursor = connection.cursor()

# Pedimos datos al usuario y le insertamos los valores a una variable
reservacion = input("Dame la fecha de tu reservacion: ").split(" ")
dia = int(reservacion[0])
mes = reservacion[1].lower()
hora = reservacion[2].lower()
no_personas = int(input("Cuantas personas? "))
# Creamos un objeto con los datos que se almacenaron en las variables
reservacion = Reservacion(dia, mes, hora, no_personas)
# Ejecutamos el metodo disponibilidad y trae el id de la reservacion si esta en la base de datos si no, una tupla vacia
disponibilidad = cursor.execute(reservacion.disponibilidad_reservacion())
disponibilidad = cursor.fetchone()
# Si la tupla tiene el id de la reservacion no hacemos la insercion de la reservacion en caso de que sea vacia se inserta
if disponibilidad:
        print("No tenemos mesa disponible, lo siento")
else:
        print("Tenemos lugar disponible")
        # Usamos el metodo insercion de la reservacion
        cursor.execute(reservacion.insercion_reservacion())
        connection.commit()
        # Buscamos el id de la reservacion y lo guardamos en una variable
        id_reservacion = cursor.execute(reservacion.busqueda_id_reservacion())
        id_reservacion = cursor.fetchone()[0]
        # Pedimos datos y los mandamos a una variable
        nombre = input("A nombre de quien la reservacion: ")
        apellido = input("Sus apellidos: ")
        correo = input("Cual es su correo? ")
        # Creamos el objeto cliente y lo insertamos en la base de datos
        cliente = Cliente(nombre, apellido, correo, id_reservacion)
        cursor.execute(cliente.insercion_cliente())
        connection.commit()