from Entidades.MysqlConnection import Mysql_Connection
from Entidades.entidad_openAi import OpenAI_Entidad
from Entidades.Reservacion import Reservacion

connection_mysql = Mysql_Connection()
connection = connection_mysql.connection
cursor = connection_mysql.connection.cursor()

open_ai = OpenAI_Entidad()
reservacion = Reservacion()
mensaje_bienvenida = f''' 
            ¡Hola! ¡Bienvenido al restaurante ! Estoy aquí para ayudarte con cualquier pregunta que tengas sobre 
            nuestro menú, horarios, reservas o cualquier otra información relacionada con nuestro restaurante. ¿En qué puedo ayudarte hoy?'''
mensaje_reservacion = f'''Restaurante: Me podrias decir en que horario seria y para cuantas personas? '''

# Si se conecto a la BD
if connection.is_connected():
    print("Se conecto")
bienvenida = "Hola"

while True:
    # Mensaje de bienvenida
    print(open_ai.uso_open_AI(bienvenida, mensaje_bienvenida))
    input_usuario = input().lower()

    # Si el usuario escribe salir se cierra el programa
    if input_usuario == "salir":
        break

    # Imprime el mensaje de que quiere hacer una reservacion
    #    print(open_ai.uso_open_AI(input_usuario, mensaje_reservacion))

    # Debe de darnos los datos de la reservacion
    print("datos")
    input_usuario = input().lower()
    print(reservacion.get_hora())


    print(reservacion.get_mes())


