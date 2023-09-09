import datetime

import openai

from mensajesOpenAi.extraccion_info import system, user_1, assistant

# _ = load_dotenv(find_dotenv())

openai.api_key = ""
peticion_sistema = "Eres un chatbot para el restaurante mexicano "


def genera_mensajes(sistema_ayuda, peticion_usuario, asistente):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": peticion_sistema + sistema_ayuda},
            {"role": "user", "content": peticion_usuario},
            {"role": "assistant", "content": asistente},
        ]
    )
    return completion.choices[0].message.content


# La respuesta del modelo se divide en 2 lo que dijo el cliente, y nuestra asistencia

def get_datos(final_user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_1},
            {"role": "assistant", "content": assistant},
            {"role": "user", "content": final_user}
        ]
    )
    return completion.choices[0].message.content


