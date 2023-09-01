class Asistencia_OpenAi:
    # Sistema Open AI
    s_bienvenida = "Bienvenida al chat"
    s_reservacion = "Pediras el dia y hora para la reservacion"
    s_personas = "Pediras el numero de personas para la reservacion"
    s_cliente = "Pediras el nombre y apellido del cliente"
    s_correo = "Pediras el correo del cliente"

    # User Open AI
    u_bienvenida = "Hola"
    u_reservacion = "Quiero hacer una reservacion"
    u_personas = "falta el numero de personas para la reservacion"
    u_cliente = "No me pediste el nombre y apellido para la reservacion"
    u_correo = "No me pediste el correo para la reservacion"

    # Assistant Open AI

    a_bienvenida = ''' 
                    ¡Hola! ¡Bienvenido al restaurante ! Estoy aquí para ayudarte con cualquier pregunta que tengas sobre 
                    nuestro nosotros ¿En qué puedo ayudarte hoy?'''
    a_reservacion = '''Me podrias indicar en que el dia y hora en que deseas realizarla, 
                        tenemos un horario de 10:00 a 23:00 de lunes a domingo'''
    a_personas = "Para cuantas personas seria la reservacion? "
    a_cliente = "A nombre de quien seria la reservacion?"
    a_correo = "Que correo seria? "
