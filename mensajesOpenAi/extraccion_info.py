import datetime

system = """Usted es un sistema inteligente e inteligente de reconocimiento de entidades nombradas (NER). Le 
          proporcionaré la definición de las entidades que necesita extraer, la oración de donde extrae las 
          entidades y el formato de salida con ejemplos."""

user_1 = "Tienes claro tu papel?"

assistant = "Claro, estoy listo para ayudarte con tu tarea NER. Por favor proporciónenme la información necesaria para comenzar."

lineas_guia = (
     """Definición de entidad:\n
     1. PERSONA: Nombre corto o nombre completo de una persona de cualquier región geográfica.\n
     2. FECHA: Formato dd/mm/aaaa . Las fechas también pueden estar en lenguaje natural, no debe de incluir el dia de la semana ni palabras entre la fecha solo dia, mes y año si es que tiene.\n
     3. HORA: Fortmato HH:mm . La hora se puede se tiene que dar en un formato de 24hrs.
     4. NOPERSONAS: Numero de personas donde puede aparecer a lado de la palabra "personas".
     Formato de salida, deben de ser listas con las entidades presentes:\n
     [PERSONA][FECHA][HORA][NOPERSONAS]\n
     Si no se presentan entidades en ninguna categoría, manténgala como Ninguna\n
     \n
     Ejemplos:\n
     \n
     1. Sentencia: El Sr. Jacob reside en Madrid desde el 12 de enero de 2015 desde las 16:00 a las cuales viven 3 personas.\n
     Salida: [Sr. Jacob][12 enero 2015][16:00][3]\n
     \n
     2. Sentencia: El Sr. Rajeev Mishra y Sunita Roy son amigos y se conocieron el 24/03/1998 a las 12:30 en donde estuvieron en una fiesta con 23 personas.\n
     Salida: [Sr. Rajeev Mishra, Sunita Roy][24/03/1998][12:30][23]\n 
     \n
     3. Sentencia: {}\n
     Salida: """
)
