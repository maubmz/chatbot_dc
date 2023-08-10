import mysql.connector
import openai


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

# La funcion primero verifica si en la base de datos no hay registro lleno
def disponibilidad_reservacion(dia, mes, hora, no_personas):
        consulta = ('''SELECT a.dia, a.mes, a.hora, a.no_personas FROM reservacion a WHERE a.dia = {} AND a.mes = "{}" 
        AND a.hora = "{}" AND a.no_personas = {}'''
                    .format(dia, mes , hora, no_personas))
        print(consulta)
        cursor.execute(consulta)
        return cursor.fetchone()


# Creamos una funcion para poder insertar registros a MYSQL
def insercion_reservacion(dia, mes, hora, no_personas):
        query_reservacion = ('''INSERT INTO reservacion(dia, mes, hora, no_personas) VALUES ({},"{}","{}",{})'''
                             .format(dia,mes,hora, no_personas))
        print(query_reservacion)
        cursor.execute(query_reservacion)
        connection.commit()

# Buscaremos el id de la reservacion
def busqueda_id_reservacion(dia, mes, hora, no_personas):
        query_id_reservacion = ('''SELECT a.id_reservacion FROM reservacion a WHERE a.dia = {} AND a.mes = "{}" AND a.hora = "{}" AND a.no_personas'''
                                .format(dia, mes, hora, no_personas))
        print(query_id_reservacion)
        cursor.execute(query_id_reservacion)
        id_reservacion = cursor.fetchone()
        return id_reservacion[0]


# Insertamos el registro del cliente, antes debe de estar insertada el registro de reservacion
def insercion_cliente(nombre, apellido, correo, id_reservacion):
        query_cliente = '''INSERT INTO cliente(nombre, apellido, correo, id_reservacion1) VALUES ("{}","{}","{}",{})'''.format(
                nombre, apellido, correo, id_reservacion)
        print(query_cliente)
        cursor.execute(query_cliente)
        connection.commit()


# Consultamos los registros
def consultar_reservacion(nombre_tabla):
        consulta = '''SELECT * FROM {}'''.format(nombre_tabla)
        print(consulta)
        cursor.execute(consulta)
        registros = cursor.fetchall()
        return registros
# Actualizaremos la reservacion
def update_reservacion(dia , mes, hora, no_personas, id_reservacion):
        consulta = ('''UPDATE reservacion SET dia = {}, mes = "{}", hora = "{}", no_personas = {} WHERE id_reservacion = {}'''
                    .format(dia, mes, hora, no_personas, id_reservacion))
        cursor.execute(consulta)
        connection.commit()
        return consulta


# Se crea todo el proceso para la reservacion
# Ingresamos la OpenIA
api_key = "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"
openai.api_key = api_key
peticion_mensaje = "Eres un chatbot donde haras las reservaciones y para eso le pediras al cliente dia, mes, hora en ese orden para realizar su reservacion"
completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
                {"role": "user", "content": peticion_mensaje}
        ]
)
print(completion.choices[0].message.content)

# Proceso del codigo para acceder a mysql
reservacion = input("Dame la fecha de tu reservacion: ").split(" ")
dia = int(reservacion[0])
mes = reservacion[1].lower()
hora = reservacion[2].lower()
no_personas = int(input("Cuantas personas? "))
resultado = disponibilidad_reservacion(dia, mes, hora, no_personas)
print(resultado)
if resultado:
        print("Lo siento, no tenemos reservaciones disponibles")
else:
        print("Buenas noticias, se esta realizando tu reservacion")

