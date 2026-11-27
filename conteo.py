def conteo(texto: str, palabras_limpias: list) -> dict:
    """Calcula las estadísticas básicas del texto y las 5 palabras
    más repetidas, y las devuelve en un diccionario"""
    num_caracter = len(texto)
    list_palabras = texto.split()
    palabras = len(list_palabras)
    cont = 0
    for palabra in list_palabras:
        cont += len(palabra)
    texto_temp = texto.replace("!", ".")
    texto_temp = texto_temp.replace("?", ".")
    texto_temp = texto_temp.split(".")
    oraciones = 0
    for oracion in texto_temp:
        if oracion.strip() != "":
            oraciones += 1
    if palabras > 0:
        division = round(cont / palabras, 2)
    else:
        division = 0
    if oraciones > 0:
        divi = round(palabras / oraciones, 2)
    else:
        divi = 0

    frecuencias = {}
    for palabra in palabras_limpias:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    top_5 = []
    for i in range(5):
        mayor = 0
        palabra_mayor = ""
        for palabra in frecuencias:
            if frecuencias[palabra] > mayor:
                mayor = frecuencias[palabra]
                palabra_mayor = palabra
        if mayor == 0:
            break
        top_5.append((palabra_mayor, mayor))
        frecuencias[palabra_mayor] = 0

    datos = {"caracteres_espacios": num_caracter,"caracteres_sin_espacios": cont,"palabras": palabras,"oraciones": oraciones,"pro_palabras": division,"pro_oraciones": divi,"top_5": top_5,}
    return datos
