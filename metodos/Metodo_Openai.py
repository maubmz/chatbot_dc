import openai

from mensajesOpenAi.asistencia_openAi import user_generar, asistente, peticion_sistema
from mensajesOpenAi.extraccion_info import system, user_1, assistant

openai.api_key = ""


# 3 roles dentro del metodo
# system: funcion que deseamos que realice,
# user:solicitud del usuario a realizar
# assistant: ejemplos de la funcion
def generador_mensajes(sistema_ayuda):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": peticion_sistema},
            {"role": "user", "content": user_generar},
            {"role": "assistant", "content": asistente},
            {"role": "system", "content": sistema_ayuda},
        ]
    )
    return completion.choices[0].message.content


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
