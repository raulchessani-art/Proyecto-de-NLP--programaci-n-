from diccionarios import words
def limpiar(texto:str) -> list:
    """Limpieza y tokenización de las palabras en base a las stopwords
    importadas desde diccionarios"""
    minusculas = texto.lower()
    signos = "!\"#$%&'()*+,-./:;<=>?@^_`{|}~¡¿[]"
    for signo in signos:
        minusculas = minusculas.replace(signo,"")
    palabras = minusculas.split()
    palabras_limpias = []
    for palabra in palabras:
        if palabra not in words and palabra.isalpha():
            palabras_limpias.append(palabra)
    return palabras_limpias