import mysql.connector

from Entidades.MysqlConnection import Mysql_Connection
from Entidades.Reservacion import Reservacion
from Entidades.Cliente import Cliente
from Entidades.entidad_openAi import OpenAI

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
        print("Conexion exitosa a la base de datos")
cursor = connection.cursor()

connection = Mysql_Connection()

# Se crea todo el proceso para la reservacion
# Ingresamos la OpenIA

reservacion_mensaje = OpenAI()
print(reservacion_mensaje.uso_open_AI())

# Pedimos datos al usuario y le insertamos los valores a una variable
dia = input()
mes = input().lower()
hora = input().lower()

no_personas = input("Cuantas personas? ")
# Creamos un objeto con los datos que se almacenaron en las variables
reservacion = Reservacion(dia, mes, hora, no_personas)

#Ejecuta la consulta a la base de datos
disponibilidad = cursor.execute(reservacion.id_reservacion())
print(reservacion.id_reservacion())

#Nos regresa el parametro solicitado en la consulta, id_reservacion
disponibilidad = cursor.fetchone()
print(disponibilidad)

# Si la tupla tiene el id de la reservacion no hacemos la insercion de la reservacion en caso de que sea vacia se inserta
if disponibilidad :
        print("No tenemos mesa disponible, lo siento")
else:
        print("Tenemos lugar disponible")
        # Usamos el metodo insercion de la reservacion
        cursor.execute(reservacion.insercion_reservacion())
        print(reservacion.insercion_reservacion())
        connection.commit()
        # Buscamos el id de la reservacion y lo guardamos en una variable
        id_reservacion = cursor.execute(reservacion.id_reservacion())
        print(reservacion.id_reservacion())
        id_reservacion = cursor.fetchone()[0]
        print(id_reservacion)
        # Pedimos datos y los mandamos a una variable
        peticion_cliente = "Le pediras al cliente su nombre, apellido y correo"
        asistente_cliente = "Dame el nombre, apellido y correo para la reservacion"
        reservacion_cliente = OpenAI(peticion_sistema, peticion_cliente, asistente_cliente)
        print(reservacion_cliente.uso_open_AI())
        nombre = input()
        apellido = input()
        correo = input()
        # Creamos el objeto cliente y lo insertamos en la base de datos
        cliente = Cliente(nombre, apellido, correo, id_reservacion)
        cursor.execute(cliente.insercion_cliente())
        print(cliente.insercion_cliente())
        connection.commit()
