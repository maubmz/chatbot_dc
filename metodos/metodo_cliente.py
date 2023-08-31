import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import ne_chunk


def encontrar_datos_cliente(texto_ususario):
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
                persona = personas.pop()
                nombre, apellido = persona.split(' ')
    return nombre, apellido


class Cliente_Reservacion:
    # Descargamos los recursos necesarios
    nltk.download('punkt')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    nltk.download('averaged_perceptron_tagger')

