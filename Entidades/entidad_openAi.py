import openai


class OpenAI_Entidad:
    openai.api_key = ""
    peticion_sistema = "Seras un chatbot de un restaurante"
    funcion_ia = "Me regresaras el apellido y nombre del texto como palabras clave"

    def uso_open_AI(self, peticion_usuario, asistente):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.peticion_sistema},
                {"role": "user", "content": peticion_usuario},
                {"role": "assistant", "content": asistente}
            ]
        )
        return completion.choices[0].message.content
# La respuesta del modelo se divide en 2 lo que dijo el cliente, y nuestra asistencia

