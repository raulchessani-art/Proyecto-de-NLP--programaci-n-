def conteo(texto:str) -> dict:
    """Calcula las estadíscticas básicas 
    del texto y las devuelve en un diccionario"""
    num_caracter = len(texto)
    list_palabras = texto.split() 
    palabras = len(list_palabras)
    cont = 0
    for palabra in list_palabras:
        cont += len(palabra)
    texto_temp =  texto.replace("!", ".")
    texto_temp = texto_temp.replace("?", ".")
    texto_temp = texto_temp.split(".")
    oraciones = 0
    for oracion in texto_temp:
        if oracion.strip() != "":
            oraciones += 1
    if palabras > 0:
        division = cont/palabras
    else:
        division = 0
    if oraciones > 0:
        divi = palabras/oraciones
    else:
        divi = 0
    datos = {"caracteres_espacios": num_caracter, "caracteres_sin_espacios": cont, "palabras": palabras, "oraciones": oraciones, "pro_palabras": division, "pro_oraciones": divi}
    return datos
