import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import ne_chunk

from fechaynombre_Reservacion.fechar_reservacion import Fecha_Reservacion

### SIRVE ESTE CODIGO
# Descargamos los recursos necesarios
class Cliente_Reservacion:

    nltk.download('punkt')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    nltk.download('averaged_perceptron_tagger')


    def extraer_informacion(self, texto_ususario):
        # Tokenizar el texto en palabras y etiquetar las palabras
        tokens = word_tokenize(texto_ususario)
        tagged_tokens = pos_tag(tokens)

        # Identificar entidades nombradas utilizando chunking
        named_entities = ne_chunk(tagged_tokens)

        # Filtrar las entidades nombradas identificadas como "PERSON" y "DATE"
        personas = []
        for entity in named_entities:
            if isinstance(entity, nltk.Tree):
                if entity.label() == 'PERSON':
                    persona = ' '.join([token for token, _ in entity.leaves()])
                    personas.append(persona)

        return personas


# Ejemplo de uso
texto_usuario = input("A nombre de quien la reservacion? ")
personas = Cliente_Reservacion()
personas = personas.extraer_informacion(texto_usuario)
print("Personas encontradas:", personas)

print("--------"*30)

mensaje = input("a que hora sera la reservacion? ")
fecha_reservacion = Fecha_Reservacion()
print(fecha_reservacion.encontrar_fecha(mensaje))


