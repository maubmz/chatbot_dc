import mysql.connector

from Objetos.Cliente import Cliente
from mensajesOpenAi.asistencia_openAi import s_bienvenida, s_reservacion, s_personas, s_cliente
from Objetos.Reservacion import Reservacion
from mensajesOpenAi.extraccion_info import lineas_guia
from metodos.Metodo_Openai import get_datos, generador_mensajes
from metodos.texto_A_lista import texto_lista

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
    print(generador_mensajes(s_bienvenida))
    input_usuario = input().lower().strip()

    # Si el usuario escribe salir se cierra el programa
    if input_usuario == "salir":
        break

    # Hacer la reservacion
    print(generador_mensajes(s_reservacion))
    input_usuario = input().lower()
    formato_input = lineas_guia.format(input_usuario)
    cadena_texto = get_datos(formato_input)
    lista_texto = texto_lista(cadena_texto)
    print(lista_texto)
    dia, mes = lista_texto[0].split(" ")
    hora = lista_texto[1]

    # Ingresar el numero de personas de la reservacion
    print(generador_mensajes(s_personas))
    no_personas = input().lower()
    formato_input = lineas_guia.format(no_personas)
    cadena_texto = get_datos(formato_input)
    lista_texto = texto_lista(cadena_texto)
    no_personas = lista_texto[0]

    print("Dia reservacion:" + dia + " Mes reservacion: " + mes + " Hora reservacion: "
          + hora + " Numero de personas: " + no_personas)


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
        cursor.execute(reservacion.insercion_reservacion())
        connection.commit()

        cursor.execute(reservacion.id_reservacion())
        id_reservacion = cursor.fetchone()[0]
        # Inserta la reservacion y pide los datos para insertar el nombre del cliente
        print(generador_mensajes(s_cliente))
        input_cliente = input()
        formato_input = lineas_guia.format(input_cliente)
        cadena_texto = get_datos(formato_input)
        lista_texto = texto_lista(cadena_texto)
        print(lista_texto)
        nombre, apellido = lista_texto[0].split(" ")

        cliente = Cliente(nombre, apellido, id_reservacion)
        cursor.execute(cliente.insercion_cliente())
        connection.commit()
        print(f"Se ha realizado con exito la reservacion para el dia {dia} del {mes} a las {hora} " +
              f"a nombre de {nombre} {apellido}")

    # Si no se pudo pregunta si quiere ingresar otra fecha?
    print("Necesitas algo mas o quieres salir?")
    input_usuario = input().lower().strip()
    if input_usuario == "salir":
        break







