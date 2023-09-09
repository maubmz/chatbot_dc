import mysql.connector

from Objetos.Cliente import Cliente
from mensajesOpenAi.asistencia_openAi import Asistencia_OpenAi
from Objetos.Reservacion import Reservacion
from metodos.Metodo_Openai import genera_mensajes
from metodos.metodo_cliente import encontrar_datos_cliente
from metodos.metodo_fecha_reservacion import encontrar_fecha
from metodos.metodo_numeropersonas import encontrar_numero_personas

mensajes_ia = Asistencia_OpenAi()

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='M1x_2021',
    database='cliente'
)

# Si se conecto a la BD
if connection.is_connected():
    print("Conexion exitosa")
cursor = connection.cursor()

while True:
    # Mensaje de bienvenida
    print(genera_mensajes(mensajes_ia.s_bienvenida, mensajes_ia.u_bienvenida, mensajes_ia.a_bienvenida))
    input_usuario = input().lower()

    # Si el usuario escribe salir se cierra el programa
    if input_usuario == "salir":
        break

    # Hacer la reservacion
    print(genera_mensajes(mensajes_ia.s_reservacion, mensajes_ia.u_reservacion, mensajes_ia.a_reservacion))
    input_usuario = input().lower()
    dia, mes, hora = encontrar_fecha(input_usuario)

    # Ingresar el numero de personas de la reservacion
    print(genera_mensajes(mensajes_ia.s_personas, mensajes_ia.u_personas, mensajes_ia.a_personas))
    no_personas = input()
    no_personas = encontrar_numero_personas(no_personas)

    # Verificacion si existe la reservacion
    print("verificando")
    reservacion = Reservacion(dia, mes, hora, no_personas)
    cursor.execute(reservacion.id_reservacion())
    disponibilidad = cursor.fetchone()

    # Si la reservacion no se puede hacer no lo inserta pero, si se puede hacer pide los datos del cliente
    if disponibilidad:
        print("No tenemos mesa disponible, lo siento")
    else:
        # Mensaje de verificacion
        print("Hay disponibilidad!")

        # Inserta la reservacion y pide los datos para insertar el nombre del cliente
        print(genera_mensajes(mensajes_ia.s_cliente, mensajes_ia.u_cliente, mensajes_ia.a_cliente))
        input_cliente = input()
        cursor.execute(reservacion.insercion_reservacion())
        connection.commit()
        cursor.execute(reservacion.id_reservacion())
        id_reservacion = cursor.fetchone()[0]
        nombre, apellido = encontrar_datos_cliente(input_cliente)

        # Pide el correo al usuario
        print(genera_mensajes(mensajes_ia.s_correo, mensajes_ia.u_correo, mensajes_ia.a_correo))
        correo = input().lower()
        cliente = Cliente(nombre, apellido, correo, id_reservacion)
        cursor.execute(cliente.insercion_cliente())
        connection.commit()
        print(f"Se ha realizado con exito la reservacion para el dia {dia} del {mes} a las {hora} " +
              f"a nombre de {nombre} {apellido}")

    # Si no se pudo pregunta si quiere ingresar otra fecha?
    print("quieres salir o probar con otra fecha?")
    input_usuario = input().lower()
    if input_usuario == "salir":
        break
