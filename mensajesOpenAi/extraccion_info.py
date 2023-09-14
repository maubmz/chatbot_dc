system = """Usted es un sistema inteligente e inteligente de reconocimiento de entidades nombradas (NER). Le 
          proporcionaré la definición de las entidades que necesita extraer, la oración de donde extrae las 
          entidades y el formato de salida con ejemplos."""

user_1 = "Tienes claro tu papel?"

assistant = "Claro, estoy listo para ayudarte con tu tarea NER. Por favor proporciónenme la información necesaria para comenzar."

lineas_guia = (
     """Definición de entidad:\n
     1. PERSONA: Nombre con Apellidos de una persona, no debes de regresar nada mas que su Nombre y Apellido.\n
     2. FECHA: Formato dd/mm/aaaa . Las fechas se presentan en lenguaje natural, no debe de incluir el dia de la semana 
     ni palabras entre la fecha solo dia, mes y año si es que tiene.\n
     3. HORA: Fortmato HH:mm . La hora se tiene que dar en un formato de 24hrs.
     4. NUMERODEPERSONAS: Numero de personas que asistieron o asistiran, se presenta como un numero entero y aparece
      cerca de la palabra "persona" o "personas", solo imprimir el numero que nos ha dado el usuario.
     Formato de salida, deben de ser listas con las entidades presentes, las entidades pueden ser encontradas en otro 
     orden pero necesito que tu las organices en el orden que te estoy asignando, ademas de no imprimir mas de lo que el 
     usuario te ingresa, no imprimir nada de los ejemplos:\n
     [PERSONA][FECHA][HORA][NUMERODEPERSONAS]\n
     Si no se presentan entidades en ninguna categoría, no debe de existir salida; en caso de que existan unas y otras 
     no, devolver las existentes nada mas\n
     \n
     Ejemplos:\n
     \n
     1. Sentencia: El Sr. Jacob reside en Madrid desde el 12 de enero de 2015 desde las 16:00 a las cuales viven 3 personas.\n
     Salida: [Sr. Jacob][12 enero 2015][16:00][3]\n
     \n
     2. Sentencia: El Sr. Rajeev Mishra y Sunita Roy son amigos y se conocieron el 24/03/1998 a las 12:30 en donde estuvieron en una fiesta con 23 personas.\n
     Salida: [Sr. Rajeev Mishra, Sunita Roy][24/03/1998][12:30][23]\n 
     \n
     3. Sentencia: A nombre de Jacob Smith
     Salida: [Jacob Smith]
     \n
     4. Sentencia: para 4 personas
     Salida: [4]
     \n
     5. Sentencia: El dia 24 de noviembre
     Salida: [24 noviembre]
     \n
     6.Setencia: A las 20:00
     Salida: [20:00]
     \n
     7. Sentencia: El dia 25 de abril a las 20:00
     Salida: [25 abril][20:00]
     \n
     8. Setencia: El nombre de Miguel Garza es un nombre muy popular
     Salida: [Miguel Garza]
     \n
     9. Setencia: Seria a las 20:40 el dia 25 de noviembre
     Salida: [25 noviembre][20:40]
     \n
     10. Sentencia: En una fiesta que realice hoy asistieron 123 personas.
     Salida: [123]
     \n
     11. Sentencia: Una mesa para 4 personas
     Salida: [4]
     \n
     12. Sentencia: {}
     Salida: """
)
