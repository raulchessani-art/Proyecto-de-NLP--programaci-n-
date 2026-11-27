from entrada_salida import validar
from conteo import conteo
from limpieza_nlp import limpiar
texto = validar()
print(texto)
palabras_limpias = limpiar(texto)
estas = conteo(texto, palabras_limpias)
print(estas)
palabras_limpias = limpiar(texto) 
