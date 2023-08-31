import re

def encontrar_numero_personas(texto):
    patron = r"\b(\d+)\s*(?:personas?)?\b"  # Patrón para buscar números seguidos de palabras relacionadas con personas

    coincidencias = re.findall(patron, texto)
    if coincidencias:
        numero_personas = int(coincidencias[0])
        return numero_personas
