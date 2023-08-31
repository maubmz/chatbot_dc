import openai


class OpenAI_Entidad:
    openai.api_key = ""
    peticion_sistema = "Eres un chatbot para el restaurante mexicano "

    def uso_open_AI(self, sistema_ayuda, peticion_usuario, asistente):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.peticion_sistema + sistema_ayuda},
                {"role": "user", "content": peticion_usuario},
                {"role": "assistant", "content": asistente},
            ]
        )
        return completion.choices[0].message.content

    # La respuesta del modelo se divide en 2 lo que dijo el cliente, y nuestra asistencia

